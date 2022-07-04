from django.urls import path
from .views import index, crear_usuario, listado_usuarios


urlpatterns = [
    path('', index, name='home'),
    path('registrarse/', crear_usuario, name='crear_usuario'),
    path('listado_usuarios/', listado_usuarios, name='listado_usuarios'),
]