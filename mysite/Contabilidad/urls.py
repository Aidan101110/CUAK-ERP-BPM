from cgitb import html
from django.urls import path
from . import views
from Contabilidad.views import Contabilidad, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', views.Contabilidad, name='Contabilidad'),
   path('registro/', views.register, name='register'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name='logout')


  
]