from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
   
    path('a/',views.about_us, name='about'),
    path('t/',views.Teacher_Info, name='t'),
]
