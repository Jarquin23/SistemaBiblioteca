from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['estudiante', 'libro']
        widgets = {
            'estudiante': forms.Select(attrs={'class':'form-control'}),
            'libro': forms.Select(attrs={'class':'form-control'}),
        }