from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.

def index(request):
    return render(request, 'index.html')


def mi_template(request):
    template = loader.get_template('vista_temp.html')
    
    nombre = 'Matias'
    
    render = template.render({'nombre':nombre})
    return HttpResponse(render)