from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import Actividad, UsuarioInscrito, Monitor, Sala, ResponsableSala
from .forms import (ActividadForm, UsuarioInscritoForm, MonitorForm, SalaForm,
                    ResponsableSalaForm, InscribirUsuarioForm)


def index(request):
    return render(request, 'gestion_actividades/index.html')

def menu_salas(request):
    return render(request, 'gestion_actividades/menu_salas.html')

#---------------------------------ACTIVIDADES---------------------------------
"""
def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'gestion_actividades/lista_actividades.html', {'actividades': actividades})
"""


def lista_actividades(request):
    tipo = request.GET.get('tipo')
    monitor_id = request.GET.get('monitor')
    actividades = Actividad.objects.all()

    if tipo:
        actividades = actividades.filter(tipo__icontains=tipo)

    if monitor_id:
        actividades = actividades.filter(monitor_id=monitor_id)

    monitores = Monitor.objects.all()

    return render(request, 'gestion_actividades/lista_actividades.html', {
        'actividades': actividades,
        'monitores': monitores,
        'tipo_actual': tipo,
        'monitor_actual': monitor_id
    })

def nueva_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_actividades')
    else:
        form = ActividadForm()
    return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Nueva Actividad'})

def detalle_actividad(request, actividad_id):
    try:
        actividad = Actividad.objects.get(id=actividad_id)
        return render(request, 'gestion_actividades/detalle_actividad.html', {'actividad': actividad})
    except Actividad.DoesNotExist:
        return JsonResponse({"error": "Actividad no encontrada"}, status=404)

def editar_actividad(request, actividad_id):
    try:
        actividad = Actividad.objects.get(id=actividad_id)
        if request.method == 'POST':
            form = ActividadForm(request.POST, instance=actividad)
            if form.is_valid():
                form.save()
                return redirect('detalle_actividad', actividad_id=actividad.id)
        else:
            form = ActividadForm(instance=actividad)
        return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Editar Actividad'})
    except Actividad.DoesNotExist:
        return JsonResponse({"error": "Actividad no encontrada"}, status=404)

def eliminar_actividad(request, actividad_id):
    try:
        actividad = Actividad.objects.get(id=actividad_id)
        if request.method == 'POST':
            actividad.delete()
            return redirect('lista_actividades')
        return render(request, 'gestion_actividades/eliminar_actividad.html', {'actividad': actividad})
    except Actividad.DoesNotExist:
        return JsonResponse({"error": "Actividad no encontrada"}, status=404)

#---------------------------------USUARIOS---------------------------------
"""
def lista_usuarios(request):
    usuarios = UsuarioInscrito.objects.all()
    return render(request, 'gestion_actividades/lista_usuarios.html', {'usuarios': usuarios})
"""
def lista_usuarios(request):
    actividad_id = request.GET.get('actividad')

    usuarios = UsuarioInscrito.objects.all()

    if actividad_id:
        usuarios = usuarios.filter(actividad__id=actividad_id)

    actividades = Actividad.objects.all()

    return render(request, 'gestion_actividades/lista_usuarios.html', {
        'usuarios': usuarios,
        'actividades': actividades,
        'actividad_actual': actividad_id
    })

def nuevo_usuario(request):
    if request.method == 'POST':
        form = UsuarioInscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioInscritoForm()
    return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Nuevo Usuario'})

def detalle_usuario(request, usuario_id):
    try:
        usuario = UsuarioInscrito.objects.get(id=usuario_id)
        return render(request, 'gestion_actividades/detalle_usuario.html', {'usuario': usuario})
    except UsuarioInscrito.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)

def editar_usuario(request, usuario_id):
    try:
        usuario = UsuarioInscrito.objects.get(id=usuario_id)
        if request.method == 'POST':
            form = UsuarioInscritoForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                return redirect('detalle_usuario', usuario_id=usuario.id)
        else:
            form = UsuarioInscritoForm(instance=usuario)
        return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Editar Usuario'})
    except UsuarioInscrito.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)

def eliminar_usuario(request, usuario_id):
    try:
        usuario = UsuarioInscrito.objects.get(id=usuario_id)
        if request.method == 'POST':
            usuario.delete()
            return redirect('lista_usuarios')
        return render(request, 'gestion_actividades/eliminar_usuario.html', {'usuario': usuario})
    except UsuarioInscrito.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)

#---------------------------------MONITORES---------------------------------

def lista_monitores(request):
    monitores = Monitor.objects.all()
    return render(request, 'gestion_actividades/lista_monitores.html', {'monitores': monitores})

def nuevo_monitor(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_monitores')
    else:
        form = MonitorForm()
    return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Nuevo Monitor'})

def detalle_monitor(request, monitor_id):
    try:
        monitor = Monitor.objects.get(id=monitor_id)
        return render(request, 'gestion_actividades/detalle_monitor.html', {'monitor': monitor})
    except Monitor.DoesNotExist:
        return JsonResponse({"error": "Monitor no encontrado"}, status=404)

def editar_monitor(request, monitor_id):
    try:
        monitor = Monitor.objects.get(id=monitor_id)
        if request.method == 'POST':
            form = MonitorForm(request.POST, instance=monitor)
            if form.is_valid():
                form.save()
                return redirect('detalle_monitor', monitor_id=monitor.id)
        else:
            form = MonitorForm(instance=monitor)
        return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Editar Monitor'})
    except Monitor.DoesNotExist:
        return JsonResponse({"error": "Monitor no encontrado"}, status=404)

def eliminar_monitor(request, monitor_id):
    try:
        monitor = Monitor.objects.get(id=monitor_id)
        if request.method == 'POST':
            monitor.delete()
            return redirect('lista_monitores')
        return render(request, 'gestion_actividades/eliminar_monitor.html', {'monitor': monitor})
    except Monitor.DoesNotExist:
        return JsonResponse({"error": "Monitor no encontrado"}, status=404)

#---------------------------------SALAS---------------------------------

def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, 'gestion_actividades/lista_salas.html', {'salas': salas})

def nueva_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_salas')
    else:
        form = SalaForm()
    return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Nueva Sala'})

def detalle_sala(request, sala_id):
    try:
        sala = Sala.objects.get(id=sala_id)
        return render(request, 'gestion_actividades/detalle_sala.html', {'sala': sala})
    except Sala.DoesNotExist:
        return JsonResponse({"error": "Sala no encontrada"}, status=404)

def editar_sala(request, sala_id):
    try:
        sala = Sala.objects.get(id=sala_id)
        if request.method == 'POST':
            form = SalaForm(request.POST, instance=sala)
            if form.is_valid():
                form.save()
                return redirect('detalle_sala', sala_id=sala.id)
        else:
            form = SalaForm(instance=sala)
        return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Editar Sala'})
    except Sala.DoesNotExist:
        return JsonResponse({"error": "Sala no encontrada"}, status=404)

def eliminar_sala(request, sala_id):
    try:
        sala = Sala.objects.get(id=sala_id)
        if request.method == 'POST':
            sala.delete()
            return redirect('lista_salas')
        return render(request, 'gestion_actividades/eliminar_sala.html', {'sala': sala})
    except Sala.DoesNotExist:
        return JsonResponse({"error": "Sala no encontrada"}, status=404)

#---------------------------------RESPONSABLES DE SALAS---------------------------------

def lista_responsables(request):
    responsables = ResponsableSala.objects.all()
    return render(request, 'gestion_actividades/lista_responsables.html', {'responsables': responsables})

def nuevo_responsable(request):
    if request.method == 'POST':
        form = ResponsableSalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_responsables')
    else:
        form = ResponsableSalaForm()
    return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Nuevo Responsable de Sala'})

def detalle_responsable(request, responsable_id):
    try:
        responsable = ResponsableSala.objects.get(id=responsable_id)
        return render(request, 'gestion_actividades/detalle_responsable.html', {'responsable': responsable})
    except ResponsableSala.DoesNotExist:
        return JsonResponse({"error": "Responsable no encontrado"}, status=404)

def editar_responsable(request, responsable_id):
    try:
        responsable = ResponsableSala.objects.get(id=responsable_id)
        if request.method == 'POST':
            form = ResponsableSalaForm(request.POST, instance=responsable)
            if form.is_valid():
                form.save()
                return redirect('detalle_responsable', responsable_id=responsable.id)
        else:
            form = ResponsableSalaForm(instance=responsable)
        return render(request, 'gestion_actividades/formulario.html', {'form': form, 'titulo': 'Editar Responsable'})
    except ResponsableSala.DoesNotExist:
        return JsonResponse({"error": "Responsable no encontrado"}, status=404)

def eliminar_responsable(request, responsable_id):
    try:
        responsable = ResponsableSala.objects.get(id=responsable_id)
        if request.method == 'POST':
            responsable.delete()
            return redirect('lista_responsables')
        return render(request, 'gestion_actividades/eliminar_responsable.html', {'responsable': responsable})
    except ResponsableSala.DoesNotExist:
        return JsonResponse({"error": "Responsable no encontrado"}, status=404)

#---------------------------------INSCRIPCIONES---------------------------------

def listar_inscripciones(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    usuarios = actividad.usuarios_inscritos.all()
    return render(request, 'gestion_actividades/lista_inscripciones.html', {
        'actividad': actividad,
        'usuarios': usuarios
    })

def inscribir_usuario(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)

    if request.method == 'POST':
        form = InscribirUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']

            if actividad.usuarios_inscritos.filter(id=usuario.id).exists():
                return render(request, 'gestion_actividades/inscribir_usuario.html', {
                    'form': form,
                    'actividad': actividad,
                    'error': f"El usuario {usuario.nombre} ya está inscrito en esta actividad."
                })

            if actividad.plazas_disponibles > 0:
                actividad.usuarios_inscritos.add(usuario)
                actividad.plazas_disponibles -= 1
                actividad.save()
                return redirect('listar_inscripciones', actividad_id=actividad.id)
            else:
                return render(request, 'gestion_actividades/inscribir_usuario.html', {
                    'form': form,
                    'actividad': actividad,
                    'error': "No quedan plazas disponibles."
                })
    else:
        form = InscribirUsuarioForm()

    return render(request, 'gestion_actividades/inscribir_usuario.html', {
        'form': form,
        'actividad': actividad,
        'titulo': f'Inscribir en {actividad.nombre}'
    })

def eliminar_inscripcion(request, actividad_id, usuario_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    usuario = get_object_or_404(UsuarioInscrito, id=usuario_id)

    if request.method == 'POST':
        if actividad.usuarios_inscritos.filter(id=usuario.id).exists():
            actividad.usuarios_inscritos.remove(usuario)
            actividad.plazas_disponibles += 1
            actividad.save()

        return redirect('listar_inscripciones', actividad_id=actividad.id)

    return render(request, 'gestion_actividades/confirmar_cancelacion.html', {
        'actividad': actividad,
        'usuario': usuario
    })