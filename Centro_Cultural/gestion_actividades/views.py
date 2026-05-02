from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Actividad, Monitor, Sala


@csrf_exempt
def lista_actividades(request):
    if request.method == 'GET':
        actividades = list(
            Actividad.objects.values(
                'id',
                'nombre',
                'tipo',
                'horario',
                'descripcion',
                'duracion',
                'plazas_disponibles'
            )
        )
        return JsonResponse(actividades, safe=False)
    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def registrar_actividad(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            monitor = Monitor.objects.get(id=data['monitor_id'])
            sala_principal = Sala.objects.get(id=data['sala_principal_id'])

            actividad = Actividad.objects.create(
                nombre=data['nombre'],
                tipo=data['tipo'],
                horario=data['horario'],
                descripcion=data['descripcion'],
                duracion=data['duracion'],
                plazas_disponibles=data['plazas_disponibles'],
                monitor=monitor,
                sala_principal=sala_principal
            )

            return JsonResponse({
                "mensaje": "Actividad registrada con éxito",
                "actividad_id": actividad.id
            })

        except Monitor.DoesNotExist:
            return JsonResponse({"error": "Monitor no encontrado"}, status=404)
        except Sala.DoesNotExist:
            return JsonResponse({"error": "Sala principal no encontrada"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def detalle_actividad(request, actividad_id):
    if request.method == 'GET':
        try:
            actividad = Actividad.objects.get(id=actividad_id)

            respuesta = {
                "id": actividad.id,
                "nombre": actividad.nombre,
                "tipo": actividad.tipo,
                "horario": actividad.horario,
                "descripcion": actividad.descripcion,
                "duracion": actividad.duracion,
                "plazas_disponibles": actividad.plazas_disponibles,
                "monitor": actividad.monitor.nombre,
                "sala_principal": actividad.sala_principal.nombre,
            }

            return JsonResponse(respuesta)

        except Actividad.DoesNotExist:
            return JsonResponse({"error": "Actividad no encontrada"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)