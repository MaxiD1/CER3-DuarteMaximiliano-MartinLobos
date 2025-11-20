from django.db import models
from django.contrib.auth.models import User

class evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    fecha_palabra = models.CharField(max_length=200)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    imagen = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField(default=100)
    inscritos = models.ManyToManyField(User, related_name='eventos_inscritos', blank=True)

    def total_inscritos(self):
        return self.inscritos.count()
    
    def hay_cupo(self):
        return (self.capacidad - self.total_inscritos())
