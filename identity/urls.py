from django.urls import path
from .views import *

app_name = 'identity'
urlpatterns = [
    path('giris/', Login.as_view(), name='login'),
    path('kaydol/', Register.as_view(), name='register'),
]