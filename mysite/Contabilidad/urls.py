from cgitb import html
from django.urls import path
from . import views
from Contabilidad.views import Contabilidad, register, Ingreso_View, Egreso_View, ImprimirReporte
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', views.Ingreso_View, name='Ingresos'),
   path('egresos/', views.Egreso_View, name='Egresos'),
   path('registro/', views.register, name='register'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   #la seguiente es la  url para la generación del pdf, el parametro <int:pk> es totalmente opcional, para utilizar en sistemas en los que se cuenta el numero de la factura por ejemplo
   path('sale/invoice/pdf/', ImprimirReporte.as_view(), name='sale_invoice_pdf'),

   

  
]