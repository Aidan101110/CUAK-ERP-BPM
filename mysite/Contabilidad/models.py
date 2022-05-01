from pickle import FALSE, TRUE
from pyexpat import model
from sqlite3 import Timestamp
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import model_to_dict
# Create your models here.

 
class Bolsillo(models.Model):
    Nombre = models.CharField(max_length=25, verbose_name='Nombre bolsillo', unique=TRUE)
    

    class Meta:
        #este va a ser la manera en la que se ordenen los datos al llamarlos desde el admin o desde las vistas
        ordering = ['id']

    def __str__(self):
        #Esto será lo que devuelva el modelo al momento de mostrarse desde el administrador, se pueden poner varios campos
        return self.Nombre


class Categoría_Ingresos(models.Model):
    Nombre = models.CharField(max_length=25, verbose_name='Nombre Categoría', unique=TRUE)
    #Monto = models.DecimalField(blank= FALSE,decimal_places=0, max_digits=13)

    class Meta:
        #este va a ser la manera en la que se ordenen los datos al llamarlos desde el admin o desde las vistas
        ordering = ['id']

    def __str__(self):
        #Esto será lo que devuelva el modelo al momento de mostrarse desde el administrador, se pueden poner varios campos
        return self.Nombre


class Categoría_Egresos(models.Model):
    Nombre = models.CharField(max_length=25, verbose_name='Nombre Categoría', unique=TRUE)
    #Monto = models.DecimalField(blank= FALSE,decimal_places=0, max_digits=13)

    class Meta:
        #este va a ser la manera en la que se ordenen los datos al llamarlos desde el admin o desde las vistas
        ordering = ['id']

    def __str__(self):
        #Esto será lo que devuelva el modelo al momento de mostrarse desde el administrador, se pueden poner varios campos
        return self.Nombre



class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image


class Ingreso(models.Model):
    timestamp = models.DateTimeField( default=timezone.now)
    Valor = models.DecimalField(null=FALSE, blank= FALSE,decimal_places=0, max_digits=10 )
    Categoría = models.ForeignKey(Categoría_Ingresos, on_delete=models.PROTECT) #El tipo de relación many to many field permite u
    Bolsillo_Afectado = models.ForeignKey(Bolsillo, on_delete=models.PROTECT) #la propiedad PROTECT indica que no se puede borrar un registro de bolsillo si otra tabla lo está usando
    Nombre = models.CharField(max_length=30, blank=FALSE, null=FALSE)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='form_ing' )

    class Meta:
        #este va a ser la manera en la que se ordenen los datos al llamarlos desde el admin o desde las vistas
        ordering = ['-timestamp']

    def __str__(self):
        #Esto será lo que devuelva el modelo al momento de mostrarse desde el administrador, se pueden poner varios campos
        return self.Nombre


class Egreso(models.Model):
    timestamp = models.DateTimeField( default=timezone.now)
    Valor = models.DecimalField(null=FALSE, blank= FALSE,decimal_places=0, max_digits=10 )
    Categoría = models.ForeignKey(Categoría_Egresos, on_delete=models.PROTECT) #El tipo de relación many to many field permite u
    Bolsillo_Afectado = models.ForeignKey(Bolsillo, on_delete=models.PROTECT) #la propiedad PROTECT indica que no se puede borrar un registro de bolsillo si otra tabla lo está usando
    Nombre = models.CharField(max_length=30, blank=FALSE, null=FALSE)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Egreso' )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.Nombre



