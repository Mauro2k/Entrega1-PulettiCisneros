from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.

def mi_vista(request):
    template = loader.get_template('vista_temp.html')
    render = template.render({})
    return HttpResponse (render)