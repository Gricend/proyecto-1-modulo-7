from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from principal.models import Tarea
from principal.forms import LoginForm

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
    tareas = Tarea.objects.filter(usuario=user, estado='pendiente').order_by('fecha_limite')
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

def detalle_tareas(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    return render(request, 'tareas/detalle_tareas.html', {'tarea': tarea})