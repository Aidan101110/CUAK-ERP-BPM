from cgitb import html
from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('', login_required(Ingreso_View.as_view()), name='Ingresos'),
   path('egresos/', login_required(Egreso_View.as_view()), name='Egresos'),
   path('registro/', views.register, name='register'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   #la seguiente es la  url para la generación del pdf, el parametro <int:pk> es totalmente opcional, para utilizar en sistemas en los que se cuenta el numero de la factura por ejemplo
   path('sale/invoice/pdf/', ImprimirReporte.as_view(), name='sale_invoice_pdf'),
   #rutas de prueba:
  # path('ingresos/', Clase_Prueba.as_view(), name='Prueba'),

   
 
  
]