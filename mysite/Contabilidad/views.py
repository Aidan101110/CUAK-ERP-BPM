from ast import For
from curses.ascii import US
from imp import reload
from multiprocessing import context
from pyexpat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.views import View
from requests import request
from .forms import Egreso_Form, Ingreso_Form, UserRegisterForm 
from .models import Ingreso, Egreso, Bolsillo
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






def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ingresos')
    else:
        form = UserRegisterForm()
        
    context = {'form':form}
    return render(request, 'registro.html', context)







class Ingreso_View(TemplateView):
    template_name = 'ingresos.html'
    model = Ingreso
    form_var = Ingreso_Form


    #función para obtener los datos de la grafica de ingresos mensuales
    def get_graph_sales_year_month(self):
            data = []
            try:
                year = datetime.now().year
                for m in range(1, 13):
                    #total = Ingreso.objects.filter(timestamp__year=year, timestamp__month=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                    total = Ingreso.objects.filter(timestamp__year=year, timestamp__month=m).aggregate(r=Coalesce(Sum('Valor'), 0, output_field=FloatField())).get('r')
                    data.append(float(total))
            except:
                pass
            return data

    def get_graph_egresos_year_month(self):
            data = []
            try:
                year = datetime.now().year
                for m in range(1, 13):
                    #total = Egreso.objects.filter(timestamp__year=year, timestamp__month=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                    total = Egreso.objects.filter(timestamp__year=year, timestamp__month=m).aggregate(r=Coalesce(Sum('Valor'), 0, output_field=FloatField())).get('r')
                    data.append(float(total))
            except:
                pass
            return data


    def get_bolsillos (self):
        bolsi = []
    
       # result = Ingreso.objects.values(Ingreso.Bolsillo_Afectado.Nombre)
        #result = Ingreso.objects.order_by(Ingreso.Bolsillo_Afectado.Nombre)
       
        #result = Ingreso.objects.aggregate(total_price=Sum('Valor'))
        result = Egreso.objects.aggregate(r=Coalesce(Sum('Valor'), 0, output_field=FloatField())).get('r')
        bolsi.append(result)

        return bolsi
  
    def post (self, request, *args, **kwargs):
        form_ing = self.form_var(request.POST)
        
        if form_ing.is_valid():
            
            Asigna_Usuario_Ingreso = form_ing.save(commit=False) #TODAS LAS VARIABLES Asigna_Usuario_Ingreso SON PARA AGREGAR AUTOMATICAMENTE AL MODELO "Usuario" EL USUARIO QUE ESTA EN SESION
            Asigna_Usuario_Ingreso.Usuario = request.user             
            Asigna_Usuario_Ingreso.save()
            return redirect('Ingresos')#aquí ponemos el nombre de la url a la que llamará

        else:
            form_ing = Ingreso_Form()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Historial_Ingresos'] = Ingreso.objects.all()
        context['Bolsillos'] = Bolsillo.objects.all()
        context['form_ing'] = self.form_var
        context['graph_sales_year_month'] = self.get_graph_sales_year_month()
        context['graph_egresos_year_month'] = self.get_graph_egresos_year_month()
        context['bolsi'] = self.get_bolsillos()

        return context




class Egreso_View(TemplateView):
    template_name = 'egresos.html'
    model = Egreso
    form_var = Egreso_Form


    #función para obtener los datos de la grafica de ingresos mensuales
    def get_graph_sales_year_month(self):
            data = []
            try:
                year = datetime.now().year
                for m in range(1, 13):
                    #total = Ingreso.objects.filter(timestamp__year=year, timestamp__month=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                    total = Ingreso.objects.filter(timestamp__year=year, timestamp__month=m).aggregate(r=Coalesce(Sum('Valor'), 0, output_field=FloatField())).get('r')
                    data.append(float(total))
            except:
                pass
            return data

    def get_graph_egresos_year_month(self):
            data = []
            try:
                year = datetime.now().year
                for m in range(1, 13):
                    #total = Egreso.objects.filter(timestamp__year=year, timestamp__month=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                    total = Egreso.objects.filter(timestamp__year=year, timestamp__month=m).aggregate(r=Coalesce(Sum('Valor'), 0, output_field=FloatField())).get('r')
                    data.append(float(total))
            except:
                pass
            return data


    def get_bolsillos (self):
        bolsi = []
    
       # result = Ingreso.objects.values(Ingreso.Bolsillo_Afectado.Nombre)
        #result = Ingreso.objects.order_by(Ingreso.Bolsillo_Afectado.Nombre)
       
        #result = Ingreso.objects.aggregate(total_price=Sum('Valor'))
        result = Egreso.objects.aggregate(r=Coalesce(Sum('Valor'), 0, output_field=FloatField())).get('r')
        bolsi.append(result)

        return bolsi
  
    def post (self, request, *args, **kwargs):
        form_Eg = self.form_var(request.POST)
        
        if form_Eg.is_valid():
            
            Asigna_Usuario_Egreso = form_Eg.save(commit=False) #TODAS LAS VARIABLES Asigna_Usuario_Ingreso SON PARA AGREGAR AUTOMATICAMENTE AL MODELO "Usuario" EL USUARIO QUE ESTA EN SESION
            Asigna_Usuario_Egreso.Usuario = request.user             
            Asigna_Usuario_Egreso.save()
            return redirect('Egresos')#aquí ponemos el nombre de la url a la que llamará

        else:
            form_ing = Egreso_Form()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Historial_Egresos'] = Egreso.objects.all()
        context['Bolsillos'] = Bolsillo.objects.all()
        context['form_Eg'] = self.form_var
        context['graph_sales_year_month'] = self.get_graph_sales_year_month()
        context['graph_egresos_year_month'] = self.get_graph_egresos_year_month()
        context['bolsi'] = self.get_bolsillos()

        return context


'''
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

'''



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



