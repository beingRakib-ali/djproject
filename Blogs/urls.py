from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
   
    path('b/',views.blog1, name='blog'),
    path('fm/',views.showRegistration, name='form'),
]
