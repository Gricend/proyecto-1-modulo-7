from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from principal.models import Tarea, Etiqueta
from principal.forms import LoginForm, FormularioTarea, FormularioEdicionTarea, ObservacionesForm

# Create your views here.

class Ingreso(TemplateView):
    template_name = 'registro/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, { "form": form })

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('lista_tareas')
            form.add_error('username', 'Credenciales incorrectas')
            return render(request, self.template_name, { "form": form })
        else:
            return render(request, self.template_name, { "form": form })
        
def lista_tarea(request):
    user = request.user
    etiquetas = Etiqueta.objects.all()
    estados = ['Pendiente', 'En Progreso', 'Completada']
    etiqueta_seleccionada = request.GET.get('etiqueta')
    estado_seleccionado = request.GET.get('estado')

    tareas = Tarea.objects.filter(user=request.user).order_by('fecha_limite')
    if etiqueta_seleccionada:
        tareas = tareas.filter(etiqueta=etiqueta_seleccionada)
    if estado_seleccionado:
        tareas = tareas.filter(estados=estado_seleccionado)    
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas, 'etiquetas':etiquetas, 'estados':estados, 'etiqueta_seleccionada':etiqueta_seleccionada, 'estado_seleccionado':estado_seleccionado })



def detalle_tareas(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    

    if request.method == 'POST':
        form = ObservacionesForm(request.POST)
        if form.is_valid():
            observaciones = form.cleaned_data['observaciones']
            tarea.observaciones = observaciones
            tarea.save()

    else:
        observaciones_anteriores = tarea.observaciones if tarea.observaciones else ''

        form = ObservacionesForm(initial={'observaciones': observaciones_anteriores})

    return render(request, 'tareas/detalle_tareas.html', {'tarea': tarea, 'form': form})

def crear_tarea(request):
    if request.method == 'POST':
        form = FormularioTarea(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.user = request.user
            tarea.save()
            return redirect('lista_tareas')
    else:
        form = FormularioTarea()

    return render(request, 'tareas/crear_tarea.html', {'form': form}) 

def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == 'POST':
        form = FormularioEdicionTarea(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('detalle_tareas', tarea.id)
    else:
        form = FormularioEdicionTarea(instance=tarea)

    return render(request, 'tareas/editar_tarea.html', {'form': form})

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('lista_tareas')

def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.estado = 'completada'
    tarea.save()
    return redirect('lista_tareas')