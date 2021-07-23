from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    s='<h1>Hello Python...</h1>'
    return HttpResponse(s)

def time_info_view(request):
    time=datetime.datetime.now()
    s='<h1>Hello Current Date and Time is :'+str(time)+'</h1>'
    return HttpResponse(s)
