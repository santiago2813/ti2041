from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Publicacion(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 200)
    categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(default = timezone.now)
    etiquetas = models.ManyToManyField('Etiqueta')

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    nombre = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    nombre = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre