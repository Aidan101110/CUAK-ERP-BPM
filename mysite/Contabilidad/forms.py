import imp
from django import forms
from django.forms import ModelForm 
from .models import Ingreso, Egreso
 

  

class Ingreso_Form (ModelForm):
    class Meta:
        model = Ingreso
        fields = '__all__'

class Egreso_Form (ModelForm):
    class Meta:
        model = Egreso
        fields = '__all__'