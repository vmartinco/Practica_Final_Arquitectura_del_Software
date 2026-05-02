from django.urls import path
from .views import (
    lista_actividades,
    nueva_actividad,
    detalle_actividad,
    editar_actividad,
    eliminar_actividad,
    lista_usuarios,
    nuevo_usuario,
    detalle_usuario,
    editar_usuario,
    eliminar_usuario,
)

urlpatterns = [
    path('actividades/', lista_actividades, name='lista_actividades'),
    path('actividades/nueva/', nueva_actividad, name='nueva_actividad'),
    path('actividades/<int:actividad_id>/', detalle_actividad, name='detalle_actividad'),
    path('actividades/<int:actividad_id>/editar/', editar_actividad, name='editar_actividad'),
    path('actividades/<int:actividad_id>/eliminar/', eliminar_actividad, name='eliminar_actividad'),

    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', nuevo_usuario, name='nuevo_usuario'),
    path('usuarios/<int:usuario_id>/', detalle_usuario, name='detalle_usuario'),
    path('usuarios/<int:usuario_id>/editar/', editar_usuario, name='editar_usuario'),
    path('usuarios/<int:usuario_id>/eliminar/', eliminar_usuario, name='eliminar_usuario'),
]