from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, CreateView
from django.core.exceptions import SuspiciousOperation
from .models import *
from .forms import *

class EntryDetail(DetailView):
    model = Entry
    context_object_name = 'entry'


class EntryList(ListView):
    model = Entry
    context_object_name = 'entries'


class EntryCreate(CreateView):
    model = Entry


class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})