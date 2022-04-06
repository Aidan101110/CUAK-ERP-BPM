from pickle import FALSE
from sqlite3 import Timestamp
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

 
Categoría_Ingreso =[
    (1, "Prestamo"),
    (2, "Only Fans"),
    (3, "Chaturbate"),
    (4, "Streamcams"),
    (5, "Streamcams1")
]

Categoría_Egreso =[
    (1, "Nominas"),
    (2, "Facturas"),
    (3, "Arrendamiento"),
    (4, "Pago de dividendos")
]

Bolsillos = [
    (1, "Cuenta corriente Davivienda"),
    (2, "Cuenta corriente Bancolombia"),
    (3, "Nequi"),
    (4, "Daviplata"),
    (5, "Efectivo (Caja)")
]


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image


class Ingreso(models.Model):
    timestamp = models.DateTimeField( auto_now_add=True)
    Valor = models.DecimalField(null=FALSE, blank= FALSE,decimal_places=0, max_digits=10 )
    Categoría = models.IntegerField(null=FALSE, blank= FALSE, choices= Categoría_Ingreso )
    Bolsillo_Afectado = models.IntegerField(null=FALSE, blank= FALSE, choices= Bolsillos)
    Nombre = models.CharField(max_length=30, blank=FALSE, null=FALSE)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Ingreso' )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.Nombre


class Egreso(models.Model):
    timestamp = models.DateTimeField( auto_now_add=True)
    Valor = models.DecimalField(null=FALSE, blank= FALSE,decimal_places=0, max_digits=10 )
    Categoría = models.IntegerField(null=FALSE, blank= FALSE, choices= Categoría_Egreso )
    Bolsillo_Afectado = models.IntegerField(null=FALSE, blank= FALSE, choices= Bolsillos)
    Nombre = models.CharField(max_length=30, blank=FALSE, null=FALSE)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Egreso' )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.Nombre



