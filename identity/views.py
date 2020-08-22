from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth import login
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
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

        except:
            raise SuspiciousOperation
