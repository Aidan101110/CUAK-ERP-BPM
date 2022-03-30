from cgitb import html
from django.urls import path
from . import views
from Contabilidad.views import Contabilidad

urlpatterns = [
   path('', views.Contabilidad, name='Contabilidad'),


  
]