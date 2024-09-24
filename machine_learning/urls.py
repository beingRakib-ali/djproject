from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    
    path('ml/',views.Machine_learning,name='ml'),
    path('knn/',views.k_nearest,name='knn'),
    path('lr/',views.linear_regression,name='lr'),
    path('rf/',views.random_forest,name='rf'),
    
]
