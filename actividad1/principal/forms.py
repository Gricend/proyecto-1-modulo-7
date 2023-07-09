from django import forms
from .models import Etiqueta, Tarea, Prioridad
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', required=True,
                                max_length=50, min_length=5,
                                error_messages={
                                    'required': 'El usuario es obligatorio',
                                    'max_length': 'El usuario no puede superar los 50 caracteres',
                                    'min_length': 'El usuario debe tener al menos 5 caracteres'
                                },
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Ingrese su usuario',
                                    'class': 'form-control'
                                })
                                )
    password = forms.CharField(label='Contraseña', required=True,
                                max_length=50, min_length=1,
                                error_messages={
                                    'required': 'La contraseña es obligatoria',
                                    'max_length': 'La contraseña no puede superar los 50 caracteres',
                                    'min_length': 'La contraseña debe tener al menos 1 caracter'
                                },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña',
                                    'class': 'form-control'
                                })
                                )


class FormularioTarea(forms.ModelForm):
    etiqueta = forms.ModelChoiceField(queryset=Etiqueta.objects.all(), label='Etiqueta')
    prioridad = forms.ModelChoiceField(queryset=Prioridad.objects.all(), label='Prioridad')
    asignado_a = forms.ModelChoiceField(queryset=User.objects.all(), label='Asignado a')

    def __init__(self, *args, **kwargs):
        super(FormularioTarea, self).__init__(*args, **kwargs)
        self.fields['etiqueta'].choices = [(etiqueta.id, etiqueta.nombre) for etiqueta in Etiqueta.objects.all()]
        self.fields['prioridad'].choices = [(prioridad.id, prioridad.nombre) for prioridad in Prioridad.objects.all()]

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_limite', 'estado', 'etiqueta', 'prioridad', 'asignado_a']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'})
        }

class FormularioEdicionTarea(forms.ModelForm):
    etiqueta = forms.ModelChoiceField(queryset=Etiqueta.objects.all(), label='Etiqueta')
    prioridad = forms.ModelChoiceField(queryset=Prioridad.objects.all(), label='Prioridad')

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_limite', 'estado', 'etiqueta', 'prioridad']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'})
        }

class ObservacionesForm(forms.Form):
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))