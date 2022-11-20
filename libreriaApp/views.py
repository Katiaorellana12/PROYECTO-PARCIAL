from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

# Create your views here.
class Home(LoginRequiredMixin , generic.TemplateView):
    template_name = 'libreriaorellana/index.html'
    login_url = '/admin'

class Home(LoginRequiredMixin , generic.TemplateView):
    template_name = 'libreriaorellana/index.html'
    login_url = 'lib:login'

def about(request):
    return render(request, "about.html")

def about2(request):
    return render(request, "about2.html")

def lte(request):
    return render(request, "lte.html")  


def index(request):
    return render(request, "index.html")

def footer(request):
    return render(request, "footer.html")