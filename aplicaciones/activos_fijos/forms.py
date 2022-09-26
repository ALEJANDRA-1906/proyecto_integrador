from datetime import datetime

from django import forms
from django.forms import ModelForm

from aplicaciones.activos_fijos.models import Activo, Empleado, Categoria, Departamento

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

        widgets = {
            'ruc': forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese ruc'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            # 'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'foto': forms.ImageField(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
        }

class ActivoForm(ModelForm):
    class Meta:
        model = Activo
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_adquisicion': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),

        }
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),




        }

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),




        }