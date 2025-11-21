from django.db import models
from django.contrib.auth.models import User

class libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    ano = models.DecimalField(max_digits=10, decimal_places=0)
    categoria = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='static/core/img', null=True, blank=True)