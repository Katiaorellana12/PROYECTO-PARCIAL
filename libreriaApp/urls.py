
from django.urls import path
from .views import *

urlpatterns = [
    
    path('index/', index), 
    path('about/' , about), 
    path('about2/' , about2), 
    path('lte/',  lte), 
]
