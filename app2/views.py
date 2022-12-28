from django.shortcuts import render

# Create your views here.
def one1(request):
    return render(request,'one1.html')

def two(request):
    return render(request,'two.html')