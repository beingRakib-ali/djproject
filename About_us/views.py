from django.http import HttpResponse
from django.shortcuts import render
from About_us.models import Teacher
# Create your views here.
def about_us(request):
    return render(request,'about/about.html')
    

def Teacher_Info(request):
    Teach=Teacher.objects.all()
    return render(request,'about/t.html',{'data': Teach})