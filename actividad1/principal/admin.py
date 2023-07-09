from django.contrib import admin
from principal.models import Etiqueta, Prioridad, Tarea

# Register your models here.

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Prioridad)
class PrioridadAdmin(admin.ModelAdmin):
    list_display = ['nombre']
