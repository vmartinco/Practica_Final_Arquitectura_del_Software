from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Actividad, UsuarioInscrito, Monitor
from .forms import ActividadForm, UsuarioInscritoForm, MonitorForm

def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'gestion_actividades/lista_actividades.html', {'actividades': actividades})


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


def lista_usuarios(request):
    usuarios = UsuarioInscrito.objects.all()
    return render(request, 'gestion_actividades/lista_usuarios.html', {'usuarios': usuarios})


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