from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

class EntryDetail(DetailView):
    model = Entry
    context_object_name = 'entry'


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

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('content:home')


class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})