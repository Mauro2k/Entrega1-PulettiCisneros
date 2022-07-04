from django import forms



class FormFormularios(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    fecha = forms.DateField(required=False)
    
