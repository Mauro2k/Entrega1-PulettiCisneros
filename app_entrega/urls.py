from django.urls import path
from .views import index, mi_template


urlpatterns = [
    path('', index),
    path('mi-template/', mi_template)
]