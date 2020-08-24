from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'identity'
urlpatterns = [
    path('giris/', LoginView.as_view(), name='login'),
    path('cikis/', LogoutView.as_view(), name='logout'),
    path('kayit/', RegisterView.as_view(), name='register'),
    path('profil/<int:pk>/', ProfileView.as_view(), name='profile'),
]