from django import forms



class FormUsuario(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    fecha = forms.DateField(required=False)
    
    
class BusquedaUsuario(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    
    
    
