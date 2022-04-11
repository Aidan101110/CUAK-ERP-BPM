from ast import For
from curses.ascii import US
from imp import reload
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import Egreso_Form, Ingreso_Form, UserRegisterForm 
from .models import Ingreso, Egreso
from django.contrib.auth.decorators import login_required



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




@login_required
def Ingreso_View(request):
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
    

    context = {'Historial_Ingresos': Historial_Ingresos,'form_ing' : form_ing}
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
