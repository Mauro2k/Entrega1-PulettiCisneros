from django.urls import path
from .views import index, crear_usuario, listado_usuarios, resenia


urlpatterns = [
    path('', index, name='home'),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),
    path('listado_usuarios/', listado_usuarios, name='listado_usuarios'),
    path('about/', resenia, name='resenia')
]