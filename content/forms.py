from django.forms import ModelForm
from .models import *

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [
            'title',
            'body',
        ]