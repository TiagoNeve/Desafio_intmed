from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(cadastrarEspecialidades)
admin.site.register(cadastrarMedicos)
admin.site.register(agendaMedica)
admin.site.register(agendaDisponivel)
admin.site.register(horariosDisponiveis)
