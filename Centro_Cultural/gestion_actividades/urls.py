from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salas/menu/', views.menu_salas, name='menu_salas'),
    #URLS ACTIVIDADES
    path('actividades/', views.lista_actividades, name='lista_actividades'),
    path('actividades/nueva/', views.nueva_actividad, name='nueva_actividad'),
    path('actividades/<int:actividad_id>/', views.detalle_actividad, name='detalle_actividad'),
    path('actividades/<int:actividad_id>/editar/', views.editar_actividad, name='editar_actividad'),
    path('actividades/<int:actividad_id>/eliminar/', views.eliminar_actividad, name='eliminar_actividad'),

    #URLS USUARIOS INSCRITOS
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.nuevo_usuario, name='nuevo_usuario'),
    path('usuarios/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/<int:usuario_id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:usuario_id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),

    #URLS DE MONITORES
    path('monitores/', views.lista_monitores, name='lista_monitores'),
    path('monitores/nuevo/', views.nuevo_monitor, name='nuevo_monitor'),
    path('monitores/<int:monitor_id>/', views.detalle_monitor, name='detalle_monitor'),
    path('monitores/<int:monitor_id>/editar/', views.editar_monitor, name='editar_monitor'),
    path('monitores/<int:monitor_id>/eliminar/', views.eliminar_monitor, name='eliminar_monitor'),

    #URLS DE SALAS
    path('salas/', views.lista_salas, name='lista_salas'),
    path('salas/nueva/', views.nueva_sala, name='nueva_sala'),
    path('salas/<int:sala_id>/', views.detalle_sala, name='detalle_sala'),
    path('salas/<int:sala_id>/editar/', views.editar_sala, name='editar_sala'),
    path('salas/<int:sala_id>/eliminar/', views.eliminar_sala, name='eliminar_sala'),

    #URLS DE RESPONSABLES DE SALAS
    path('responsables/', views.lista_responsables, name='lista_responsables'),
    path('responsables/nuevo/', views.nuevo_responsable, name='nuevo_responsable'),
    path('responsables/<int:responsable_id>/', views.detalle_responsable, name='detalle_responsable'),
    path('responsables/<int:responsable_id>/editar/', views.editar_responsable, name='editar_responsable'),
    path('responsables/<int:responsable_id>/eliminar/', views.eliminar_responsable, name='eliminar_responsable'),

    #URLS DE INSCRIPCIONES
    path('actividades/<int:actividad_id>/inscripciones/', views.listar_inscripciones, name='listar_inscripciones'),
    path('actividades/<int:actividad_id>/inscribir/', views.inscribir_usuario, name='inscribir_usuario'),
    path('actividades/<int:actividad_id>/inscripciones/<int:usuario_id>/eliminar/', views.eliminar_inscripcion, name='eliminar_inscripcion')
]