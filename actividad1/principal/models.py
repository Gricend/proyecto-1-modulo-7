from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    nombre = models.CharField(max_length=50)

    def str(self):
        return self.nombre

class Tarea(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self):
        return self.titulo