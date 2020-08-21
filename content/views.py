from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import *

class EntryDetail(DetailView):
    model = Entry
    context_object_name = 'entry'
