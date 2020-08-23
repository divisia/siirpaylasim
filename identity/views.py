from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

class RegisterView(View):
    template = 'registration/login.html'

    def get(self, request):
        return render(request, self.template, {'form': UserCreationForm()})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        try:
            if not form.is_valid():
                return render(request, self.template, {'form': form})
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(settings.LOGIN_REDIRECT_URL)

        except:
            raise SuspiciousOperation
