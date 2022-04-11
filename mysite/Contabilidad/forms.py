from dataclasses import fields
import imp
from django import forms
from django.forms import ModelForm 
from .models import Ingreso, Egreso
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #Aquí importamos nuestro modelos de usuario
 
 
  

class Ingreso_Form (ModelForm):
    class Meta:
        model = Ingreso
        fields = ['Valor', 'Categoría', 'Bolsillo_Afectado', 'Nombre']
   

class Egreso_Form (ModelForm):
    class Meta:
        model = Egreso
        fields = ['Valor', 'Categoría', 'Bolsillo_Afectado', 'Nombre']




#Clase de registro de usuario
class UserRegisterForm(UserCreationForm):
    class Meta:
        #Con esta variable asociamos nuestro formulario a la tabla usuario
        model = User
        #el siguiente bloque 'widgets' y su contenido se usa para definir los placeholders de los inputs 
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Tu nombre', 'class':'form-control form-control-user', 'id':'exampleFirstName'}),
            'username': forms.TextInput(attrs={'placeholder': 'Tu apodo', 'class':'form-control form-control-user', 'id':'exampleFirstName'}),
            'email': forms.EmailInput(attrs={'placeholder': 'alguien@ejemplo.com', 'class':'form-control form-control-user', 'id':'exampleInputEmail'}),
            'password1': forms.PasswordInput(attrs={ 'class':'form-control form-control-user', 'id':'exampleFirstName'}),
            'password2': forms.PasswordInput(attrs={ 'class':'form-control form-control-user', 'id':'exampleFirstName'})
            }
        fields = ['first_name', 'username', 'email', 'password1', 'password2']