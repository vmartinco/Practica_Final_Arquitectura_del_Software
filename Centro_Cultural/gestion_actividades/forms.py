from django import forms
from .models import Actividad, UsuarioInscrito, Monitor


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        exclude = ['usuarios_inscritos']


class UsuarioInscritoForm(forms.ModelForm):
    class Meta:
        model = UsuarioInscrito
        fields = '__all__'


class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'