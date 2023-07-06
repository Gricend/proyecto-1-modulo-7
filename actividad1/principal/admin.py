from django.contrib import admin
from principal.models import Etiqueta

# Register your models here.

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ['nombre']