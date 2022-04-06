import imp
from django import forms
from django.forms import ModelForm 
from .models import Ingreso, Egreso
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #Aquí importamos nuestro modelos de usuario
 
 
  

class Ingreso_Form (ModelForm):
    class Meta:
        model = Ingreso
        fields = '__all__'

class Egreso_Form (ModelForm):
    class Meta:
        model = Egreso
        fields = '__all__'


#Clase de registro de usuario
class UserRegisterForm(UserCreationForm):
    class Meta:
        #Con esta variable asociamos nuestro formulario a la tabla usuario
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']