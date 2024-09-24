from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Machine_learning(request):
    course = 'Machine Learning'
    seat = 20
    Total_class = 50
    duration = '6 month''s'

    """_summary_
     in ML_Dictionary there are some key which is 'c,st,tc,d' this key is contain variable(course,seat,Total_class,duration) value.
     when this key is use in html file then it called by variable. in views.py file it called key.

    Returns:
        _type_: _description_
        this all key and variable assign in a dictionary this dictionary is assign in context for render.
    """
      
    ML_Dictionary = {
                     'c':course ,
                     'st':seat,
                     'tc':Total_class,
                     'd':duration
                     }
    
    Teachers ={'names':['Rakib','Sakib','Abdullah']}
    
    """context = {
        **ML_Dictionary,  # Unpack ML_Dictionary into the context
        'Teachers': Teachers,  # Add Teachers to the context
    }"""
    
    return render(request,'machine_learning/machine_learning.html', context=Teachers)

def random_forest(request):
    return render(request,'machine_learning/random_forest.html')

def k_nearest(request):
    return render(request,'machine_learning/knn.html')

def linear_regression(request):
    return render(request,'machine_learning/linear_regression.html')
    