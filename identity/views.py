from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.conf import settings
from .forms import UserProfileForm

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('content:home')

class RegisterView(View):
    template = 'registration/register.html'

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


class UserDetail(View):
    template = 'auth/user_detail.html'

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=404)
        return render(request, self.template, {
            'editable': request.user == user,
            'user': user,
            'form': UserProfileForm(instance=user.profile),
        })


    def post(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponse('Forbidden', status=403)
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if not form.is_valid():
            return render(request, self.template, {
                'editable': request.user == user,
                'user': user,
                'form': form,
            })
        profile = form.save()
        return redirect(reverse('identity:user_detail', kwargs={'pk':request.user.pk}))



class UserList(ListView):
    model = User
    context_object_name = 'users'
