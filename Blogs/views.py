from django.http import HttpResponse
from django.shortcuts import render

from . forms import TeacherFormregistration

# Create your views here.
def blog1(request):
    return render(request,'blogs/blogs.html')

def showRegistration(request):
    fm=TeacherFormregistration()
    fm.order_fields(field_order=['frist_name','last_name','email'])
    return render(request,'blogs/form.html',{'form':fm})
    