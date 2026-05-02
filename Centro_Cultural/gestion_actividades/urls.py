from django.urls import path
from .views import (
    lista_actividades,
    nueva_actividad,
    detalle_actividad,
    editar_actividad,
    eliminar_actividad,
)

urlpatterns = [
    path('actividades/', lista_actividades, name='lista_actividades'),
    path('actividades/nueva/', nueva_actividad, name='nueva_actividad'),
    path('actividades/<int:actividad_id>/', detalle_actividad, name='detalle_actividad'),
    path('actividades/<int:actividad_id>/editar/', editar_actividad, name='editar_actividad'),
    path('actividades/<int:actividad_id>/eliminar/', eliminar_actividad, name='eliminar_actividad'),
]