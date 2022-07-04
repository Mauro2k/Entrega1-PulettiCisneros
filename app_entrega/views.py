from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from datetime import datetime

from .forms import FormFormularios
from .models import Formularios


# Create your views here.

def index(request):
    return render(request, 'index.html')


def crear_usuario(request):
    print(request.method)
    if request.method == 'POST':
        form = FormFormularios(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fecha = data.get('fecha')
            formulario = Formularios(nombre=data.get('nombre'),
                                     edad=data.get('edad'),
                                     fecha=fecha if fecha else datetime.now()
                                     )
            formulario.save()
            
            listado_usuarios = Formularios.objects.all()
            return render(request, 'listado_usuarios.html', {'listado_usuarios': listado_usuarios})        
        else:
            return render(request, 'crear_usuario.html', {'form':form})    
            
    
    formularios = FormFormularios()
    
    return render(request, 'crear_usuario.html', {'form':formularios})


def listado_usuarios(request):
    listado_usuarios = Formularios.objects.all()
    return render(request, 'listado_usuarios.html', {'listado_usuarios': listado_usuarios})