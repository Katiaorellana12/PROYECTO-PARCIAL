
from django.urls import path
from .views import *
from .views import Home

urlpatterns = [
    
    path('', Home.as_view(), name="home"), 
    path('login/', auth_views.LoginView.as_view(template_name='libreriaorellana/login.html'), name='login'), 
    path('about/' , about), 
    path('about2/' , about2), 
    path('lte/',  lte),
    path('index/',  index), 
    path('footer/',  footer), 

]
