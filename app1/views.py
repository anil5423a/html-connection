from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def string1(request):
    return HttpResponse('<h1> this is app1 first string</h1>')

def string2(request):
    return HttpResponse('<h1> this is app1 second string</h1>')