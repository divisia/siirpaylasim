from django.urls import path
from .views import *

app_name = 'content'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('siir/', EntryList.as_view(), name='entry_list'),
    path('siir/<slug:slug>/', EntryDetail.as_view(), name='entry_detail'),
    path('siir/<slug:slug>/duzenle/', EntryUpdate.as_view(), name='entry_edit'),
    path('siir/<slug:slug>/sil/', EntryDelete.as_view(), name='entry_delete'),
    path('yeni-siir/', EntryCreate.as_view(), name='entry_create'),
]