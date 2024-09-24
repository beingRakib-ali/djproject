from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
   
    path('da/',views.data_analyst, name='data'),
]
