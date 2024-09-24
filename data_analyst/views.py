from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def data_analyst(request):
    return render(request,'data_analyst/data_analyst.html')
    