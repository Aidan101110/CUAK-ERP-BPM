from cgitb import html
from django.urls import path
from . import views
from Contabilidad.views import Contabilidad, register, Ingreso_View, Egreso_View
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('ingresos/', views.Ingreso_View, name='Ingresos'),
   path('egresos/', views.Egreso_View, name='Egresos'),
   path('registro/', views.register, name='register'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),


  
]