from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def about2(request):
    return render(request, "about2.html")

def lte(request):
    return render(request, "lte.html")  