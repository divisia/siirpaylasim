from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from pinax.likes.models import Like
from datetime import date, timedelta
from .models import *
from .forms import *


highlighted_interval = timedelta(weeks=1)


class EntryDetail(DetailView):
    model = Entry
    context_object_name = 'entry'

    def get_context_data(self, *args, **kwargs):
        ctx = super(EntryDetail, self).get_context_data(*args, **kwargs)
        ctx['editable'] = self.request.user == self.get_object().author
        return ctx


class EntryList(ListView):
    model = Entry
    context_object_name = 'entries'

    def get_context_data(self, *args, **kwargs):
        ctx = super(EntryList, self).get_context_data(*args, **kwargs)
        ctx['selected'] = get_entry_with_most_likes(
            after=date.today()-highlighted_interval
        )
        return ctx


class EntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['title', 'body']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.object)


class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ['title', 'body']

    def get_object(self, *args, **kwargs):
        entry = super(EntryUpdate, self).get_object(*args, **kwargs)
        if entry.author != self.request.user:
            raise PermissionDenied
        return entry
    
    def get_success_url(self, *args, **kwargs):
        return reverse('content:entry_detail', kwargs={'slug': self.object.slug})

        

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('content:home')

    def get_object(self, *args, **kwargs):
        entry = super(EntryUpdate, self).get_object(*args, **kwargs)
        if entry.author != self.request.user:
            raise PermissionDenied
        return entry


class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})



def get_entry_with_most_likes(after=None, before=None):
    qs = Entry.objects.all()
    if after:
        qs = qs.filter(created_at__gte=after)
    if before:
        qs = qs.filter(created_at__lte=before)
    
    selected = {'count': -1}
    for entry in qs:
        count = Like.objects.filter(
            receiver_content_type=ContentType.objects.get_for_model(entry),
            receiver_object_id=entry.pk,
        ).count()
        if count > selected['count']:
            selected['pk'] = entry.pk
            selected['count'] = count
            selected['entry'] = entry

    return selected
    
