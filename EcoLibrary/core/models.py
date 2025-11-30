from django.db import models
from django.contrib.auth.models import User

class libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.IntegerField()
    imagen = models.URLField(blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    library_id = models.CharField(max_length=255)
    favoritos = models.ManyToManyField(User, related_name='favoritos', blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"