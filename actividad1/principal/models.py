from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    STATUS_CHOICES = (
        ('pendiente','Pendiente'),
        ('En progreso','En progreso'),
        ('completada', 'Completada'),
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True, max_length=200)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
    
    def get_estado_display(self):
        for choice in self.STATUS_CHOICES:
            if choice[0] == self.estado:
                return choice[1]
        return self.estado.lower()


