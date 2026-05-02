from django.contrib import admin
from .models import ResponsableSala, Monitor, UsuarioInscrito, Sala, Actividad

admin.site.register(ResponsableSala)
admin.site.register(Monitor)
admin.site.register(UsuarioInscrito)
admin.site.register(Sala)
admin.site.register(Actividad)