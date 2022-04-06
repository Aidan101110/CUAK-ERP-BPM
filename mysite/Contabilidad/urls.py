from cgitb import html
from django.urls import path
from . import views
from Contabilidad.views import Contabilidad, register

urlpatterns = [
   path('', views.Contabilidad, name='Contabilidad'),
   path('registro/', views.register, name='register'),



  
]