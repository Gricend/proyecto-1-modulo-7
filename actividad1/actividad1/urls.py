"""
URL configuration for actividad1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal.views import Ingreso, detalle_tareas, lista_tarea, crear_tarea, editar_tarea
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Ingreso.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('lista_tareas/', lista_tarea, name='lista_tareas'),
    path('detalle_tareas/<int:tarea_id>/', detalle_tareas, name='detalle_tareas'),
    path('crear_tarea/', crear_tarea, name='crear_tarea'),
    path('editar_tarea/<int:tarea_id>/', editar_tarea, name='editar_tarea'),
]
