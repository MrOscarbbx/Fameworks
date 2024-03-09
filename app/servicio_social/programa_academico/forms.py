from django import forms
from .models import UnidadAcademica,ProgramaAcademico

class FormUnidadAcademica(forms.ModelForm):
    class Meta:
        model = UnidadAcademica
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Texto'
                    }),
            'descripcion' : forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Texto'
                    })
        }

class FormProgramaAcademico(forms.ModelForm):
    class Meta:
        model = ProgramaAcademico
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Texto'
                    }),
            'descripcion' : forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Texto'
                    }),
            'unidad_academica' : forms.Select(
                attrs={
                'class' : 'form-control'
                }
            )
        }

class FormFiltroPrograma(forms.ModelForm):
    nombre = forms.TextInput(required = False)
    descripcion = forms.TextInput(required = False)
    unidad = forms.TextInput(required = False)