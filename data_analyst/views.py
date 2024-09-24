from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def data_analyst(request):
    return render(request, 'data_analyst/data_analyst.html')

class DataAnalyst(View): 
    def get(self, request):   
        return render(request, 'data_analyst/class.html')

