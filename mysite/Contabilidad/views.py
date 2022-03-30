from imp import reload
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import Egreso_Form, Ingreso_Form

# Create your views here.




def Contabilidad(request):
    if request.method == 'POST':
        Ingreso = Ingreso_Form(request.POST, prefix='Ingreso')
        if Ingreso.is_valid():
            Ingreso.save()
            return redirect(Contabilidad)
    else:
        Ingreso = Ingreso_Form(prefix='Ingreso')

    if request.method == 'POST' and not Ingreso.is_valid():
        Egreso = Egreso_Form(request.POST, prefix='Egreso')
        Ingreso = Ingreso_Form(prefix='Ingreso')
        if Egreso.is_valid():
            Egreso.save()
            return redirect(Contabilidad)

    else:
        Egreso = Egreso_Form(prefix='Egreso')

    context = {'Ingreso' : Ingreso, 'Egreso' : Egreso}
    return render (request, 'inicio.html', context)



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