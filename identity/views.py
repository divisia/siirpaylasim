from django.shortcuts import render
from django.views import View


class Login(View):
    template = 'identity/login.html'

    def get(self, request):
        return render(request, self.template, {})


class Register(View):
    template = 'identity/register.html'
    def get(self, request):
        return render(request, self.template, {})