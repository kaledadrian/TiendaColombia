from django import forms
from .models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'color', 'icono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Transporte'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Descripción de la categoría'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'icono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'bi-bus-front'}),
        }
