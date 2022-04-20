from ast import For
from curses.ascii import US
from imp import reload
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.views import View
from .forms import Egreso_Form, Ingreso_Form, UserRegisterForm 
from .models import Ingreso, Egreso
from django.contrib.auth.decorators import login_required

#Importaciónes para la grafica de ingresos mensuales
from datetime import datetime
from django.db.models.functions import Coalesce
from django.db.models import Sum
from django.db.models import FloatField
#esta importación es para crear vistas basadas en clases
from django.views.generic import TemplateView

#Importaciones para la libreria del generador del pdf xhtml2pdf
import os
from mysite import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa


def Contabilidad(request):
    Historial_Ingresos = Ingreso.objects.all() #CON ESTA LINEA LLAMAMO LOS DATOS DEL MODELO INGRESO PARA MOSTRARLOS DESPUES A TRAVES DEL CONTEXTO
    Historial_Egresos = Egreso.objects.all() #CON ESTA LINEA LLAMAMO LOS DATOS DEL MODELO EGRESO PARA MOSTRARLOS DESPUES A TRAVES DEL CONTEXTO


    if request.method == 'POST':
        Vista_Ingreso = Ingreso_Form(request.POST, prefix='Ingreso')
        if Vista_Ingreso.is_valid():
            Asigna_Usuario_Ingreso = Vista_Ingreso.save(commit=False) #TODAS LAS VARIABLES Asigna_Usuario_Ingreso SON PARA AGREGAR AUTOMATICAMENTE AL MODELO "Usuario" EL USUARIO QUE ESTA EN SESION
            Asigna_Usuario_Ingreso.Usuario = request.user             
            Asigna_Usuario_Ingreso.save() 

            return redirect(Contabilidad)
    else:
        Vista_Ingreso = Ingreso_Form(prefix='Ingreso')

    if request.method == 'POST' and not Vista_Ingreso.is_valid():
        Vista_Egreso = Egreso_Form(request.POST, prefix='Egreso')
        Vista_Ingreso = Ingreso_Form(prefix='Ingreso')
        if Vista_Egreso.is_valid():
            Asigna_Usuario_Egreso = Vista_Egreso.save(commit=False) #TODAS LAS VARIABLES Asigna_Usuario_Egreso SON PARA AGREGAR AUTOMATICAMENTE AL MODELO "Usuario" EL USUARIO QUE ESTA EN SESION
            Asigna_Usuario_Egreso.Usuario = request.user             
            Asigna_Usuario_Egreso.save() 
            return redirect(Contabilidad)

    else:
        Vista_Egreso = Egreso_Form(prefix='Egreso')

    context = {'Historial_Ingresos': Historial_Ingresos,'Historial_Egresos': Historial_Egresos, 'Vista_Ingreso' : Vista_Ingreso, 'Vista_Egreso' : Vista_Egreso}
    return render (request, 'inicio.html', context)   



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Contabilidad)
    else:
        form = UserRegisterForm()
        
    context = {'form':form}
    return render(request, 'registro.html', context)




#función para obtener los datos de la grafica de ingresos mensuales
def get_graph_sales_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = Ingreso.objects.filter(timestamp__year=year, timestamp__month=m).aggregate(r=Coalesce(Sum('total'), 0, output_field=FloatField())).get('r')
                data.append(float(total))
        except:
            pass
        return data


@login_required
def Ingreso_View(request):
    Info_Data = get_graph_sales_year_month
    Historial_Ingresos = Ingreso.objects.all() #CON ESTA LINEA LLAMAMO LOS DATOS DEL MODELO INGRESO PARA MOSTRARLOS DESPUES A TRAVES DEL CONTEXTO


    form_ing = Ingreso_Form()

    if request.method == 'POST':
        form_ing = Ingreso_Form(request.POST)
        if form_ing.is_valid():
            Asigna_Usuario_Ingreso = form_ing.save(commit=False) #TODAS LAS VARIABLES Asigna_Usuario_Ingreso SON PARA AGREGAR AUTOMATICAMENTE AL MODELO "Usuario" EL USUARIO QUE ESTA EN SESION
            Asigna_Usuario_Ingreso.Usuario = request.user             
            Asigna_Usuario_Ingreso.save()
            return redirect(Ingreso_View)

        else:
            form_ing = Ingreso_Form()
    

    context = {'Historial_Ingresos': Historial_Ingresos,'form_ing' : form_ing, 'Info_Data':Info_Data}
    return render (request, 'ingresos.html', context) 




@login_required
def Egreso_View(request):
    Historial_Egresos = Egreso.objects.all() #CON ESTA LINEA LLAMAMO LOS DATOS DEL MODELO INGRESO PARA MOSTRARLOS DESPUES A TRAVES DEL CONTEXTO


    form_Eg = Egreso_Form()

    if request.method == 'POST':
        form_Eg = Egreso_Form(request.POST)
        if form_Eg.is_valid():
            Asigna_Usuario_Egreso = form_Eg.save(commit=False) #TODAS LAS VARIABLES Asigna_Usuario_Egreso SON PARA AGREGAR AUTOMATICAMENTE AL MODELO "Usuario" EL USUARIO QUE ESTA EN SESION
            Asigna_Usuario_Egreso.Usuario = request.user             
            Asigna_Usuario_Egreso.save()
            return redirect(Egreso_View)

        else:
            form_ing = Ingreso_Form()
    

    context = {'Historial_Egresos': Historial_Egresos,'form_Eg' : form_Eg}
    return render (request, 'egresos.html', context) 





class ImprimirReporte(View):
    def get (self, request, *args, **kwargs):
        template = get_template('ingresos.html')
        context = {'title': 'Mi primer pdf'}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        #esta opción es para desargar sin vista previa el pdf >>> response['Content-Disposition' ] = 'attachment; filename="report.pdf"'
        pisaStatus = pisa.CreatePDF (
            html, dest=response)
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response  





