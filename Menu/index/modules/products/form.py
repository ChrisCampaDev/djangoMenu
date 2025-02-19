from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'gramaje', 'descripcion', 'tipo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }