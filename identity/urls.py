from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'identity'
urlpatterns = [
    path('giris/', LoginView.as_view(), name='login'),
    path('cikis/', LogoutView.as_view(), name='logout'),
    path('kayit/', RegisterView.as_view(), name='register'),
]