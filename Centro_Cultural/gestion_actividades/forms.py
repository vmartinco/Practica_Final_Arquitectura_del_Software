from django import forms
from .models import Actividad, UsuarioInscrito, Monitor, Sala, ResponsableSala


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

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class ResponsableSalaForm(forms.ModelForm):
    class Meta:
        model = ResponsableSala
        fields = '__all__'

class InscribirUsuarioForm(forms.Form):
    usuario = forms.ModelChoiceField(
        queryset=UsuarioInscrito.objects.all(),
        label="Seleccionar Usuario",
        widget=forms.Select(attrs={'class': 'form-control'})
    )