from django import forms
from .models import Actividad


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        exclude = ['usuarios_inscritos'] #Para que en Nueva Actividad y en Editar no aparezca "Usuarios inscritos"