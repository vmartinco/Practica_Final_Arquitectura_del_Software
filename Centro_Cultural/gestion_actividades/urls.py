from django.urls import path
from .views import lista_actividades, registrar_actividad, detalle_actividad

urlpatterns = [
    path('actividades/', lista_actividades, name='lista_actividades'),
    path('actividades/registrar/', registrar_actividad, name='registrar_actividad'),
    path('actividades/<int:actividad_id>/', detalle_actividad, name='detalle_actividad'),
]