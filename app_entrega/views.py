from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from datetime import datetime

from .forms import BusquedaUsuario, FormUsuario
from .models import Usuario


# Create your views here.

def index(request):
    return render(request, 'index.html')

def resenia(request):
    return render(request, 'resenia.html')


def crear_usuario(request):
    print(request.method)
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fecha = data.get('fecha')
            formulario = Usuario(nombre=data.get('nombre'),
                                     edad=data.get('edad'),
                                     fecha=fecha if fecha else datetime.now()
                                     )
            formulario.save()
            
            return redirect('listado_usuarios')     
           
        else:
            return render(request, 'crear_usuario.html', {'form':form})    
            
    
    formularios = FormUsuario()
    
    return render(request, 'crear_usuario.html', {'form':formularios})


def listado_usuarios(request):
    nombre_busqueda = request.GET.get('nombre')
    if nombre_busqueda:
        listado_usuarios = Usuario.objects.filter(nombre__icontains =nombre_busqueda) 
    else:    
        listado_usuarios = Usuario.objects.all()
    
    form = BusquedaUsuario()
    return render(request, 'listado_usuarios.html', {'listado_usuarios': listado_usuarios, 'form': form})