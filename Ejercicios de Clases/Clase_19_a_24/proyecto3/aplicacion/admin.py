from django.contrib import admin
from .models import *

# Registrar modelos aqui 
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)