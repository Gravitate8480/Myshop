from django import forms
from .models import Product

class Formulario_producto(forms.ModelForm):
    class Meta:
        model = Product
        #fields = ['name', 'price']
        fields = '__all__'
    
    
    