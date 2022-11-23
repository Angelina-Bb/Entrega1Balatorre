from django import forms

class ProductoFormulario(forms.Form):    
    cliente = forms.CharField(max_length=25)
    email = forms.EmailField()
    nombre = forms.CharField(max_length=30)
    droga = forms.CharField(max_length=25)
    laboratorio = forms.CharField(max_length=30)
    codigo = forms.IntegerField()
    stock = forms.BooleanField()
    precio = forms.IntegerField()