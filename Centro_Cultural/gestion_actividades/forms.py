from django import forms
from .models import Actividad, UsuarioInscrito


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        exclude = ['usuarios_inscritos']


class UsuarioInscritoForm(forms.ModelForm):
    class Meta:
        model = UsuarioInscrito
        fields = '__all__'