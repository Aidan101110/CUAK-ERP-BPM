from ast import For
from curses.ascii import US
from imp import reload
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import Egreso_Form, Ingreso_Form, UserRegisterForm 
from .models import Ingreso, Egreso

# Create your views here.




def Contabilidad(request):
    Historial_Ingresos = Ingreso.objects.all() #CON ESTA LINEA LLAMAMO LOS DATOS DEL MODELO INGRESO PARA MOSTRARLOS DESPUES A TRAVES DEL CONTEXTO
    Historial_Egresos = Egreso.objects.all() #CON ESTA LINEA LLAMAMO LOS DATOS DEL MODELO EGRESO PARA MOSTRARLOS DESPUES A TRAVES DEL CONTEXTO


    if request.method == 'POST':
        Vista_Ingreso = Ingreso_Form(request.POST, prefix='Ingreso')
        if Vista_Ingreso.is_valid():
            Asigna_Usuario = Vista_Ingreso.save(commit=False)
            Asigna_Usuario.Usuario = request.user
            Asigna_Usuario.save() 

            return redirect(Contabilidad)
    else:
        Vista_Ingreso = Ingreso_Form(prefix='Ingreso')

    if request.method == 'POST' and not Vista_Ingreso.is_valid():
        Vista_Egreso = Egreso_Form(request.POST, prefix='Egreso')
        Vista_Ingreso = Ingreso_Form(prefix='Ingreso')
        if Vista_Egreso.is_valid():
            Vista_Egreso.save()
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








'''

    
    
def create(request):

    form = ProductForm()


    if request.method == 'POST': 
            #print(request.POST['title'])
            form = ProductForm (request.POST)

            if form.is_valid():
                print ('valido')
                form.save()
                return redirect(create)


            else:
                print('invalido')

    context = {'form': form}
    return render (request, 'create.html', context )

'''


'''
def Contabilidad(request):
    form_ing = Ingreso_Form()
    form_Eg = Egreso_Form()

    if request.method == 'POST':
        form_ing = Ingreso_Form(request.POST)
        if form_ing.is_valid():
            form_ing.save()

    if request.method == 'POST':
        form_Eg = Egreso_Form(request.POST)
        if form_Eg.is_valid():
            form_Eg.save()

    

    context = {'form_ing' : form_ing, 'form_Eg' : form_Eg}
    return render (request, 'inicio.html', context) 
'''