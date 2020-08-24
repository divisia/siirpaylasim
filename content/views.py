from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

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