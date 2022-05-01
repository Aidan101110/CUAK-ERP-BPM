from django.contrib import admin
from .models import Ingreso, Egreso, Bolsillo, Categoría_Egresos, Categoría_Ingresos

# Register your models here.


admin.site.register(Ingreso)
admin.site.register(Egreso)
admin.site.register(Bolsillo)
admin.site.register(Categoría_Ingresos)
admin.site.register(Categoría_Egresos)
