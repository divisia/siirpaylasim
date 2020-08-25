from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import *

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [
            'title',
            'body',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Başlık'}),
            'body': forms.Textarea(attrs={'placeholder': 'Şiir metni'}),
        }