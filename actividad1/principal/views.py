from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from principal.models import Tarea, Etiqueta
from principal.forms import LoginForm, FormularioTarea
from django.contrib.auth.decorators import login_required

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

    tareas = Tarea.objects.filter(user=user, estado='pendiente').order_by('fecha_limite')
    if etiqueta_seleccionada:
        tareas = tareas.filter(etiqueta=etiqueta_seleccionada)
    if estado_seleccionado:
        tareas = tareas.filter(estado=estado_seleccionado)    
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas, 'etiquetas':etiquetas, 'estados':estados, 'etiqueta_seleccionada':etiqueta_seleccionada, 'estado_seleccionado':estado_seleccionado })



def detalle_tareas(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    return render(request, 'tareas/detalle_tareas.html', {'tarea': tarea})



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