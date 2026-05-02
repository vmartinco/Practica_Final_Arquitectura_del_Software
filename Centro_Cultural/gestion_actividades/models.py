from django.db import models

class ResponsableSala(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=100)
    numero_actividades_asignadas = models.IntegerField()

    def __str__(self):
        return self.nombre

class UsuarioInscrito(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    responsable = models.OneToOneField(ResponsableSala, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    plazas_disponibles = models.IntegerField()

    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    usuarios_inscritos = models.ManyToManyField(UsuarioInscrito, blank=True)
    sala_principal = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='sala_principal_actividad')
    salas_secundarias = models.ManyToManyField(Sala, related_name='salas_secundarias_actividad', blank=True)

    def __str__(self):
        return self.nombre