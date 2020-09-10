from rest_framework import serializers
from .models import *

class especialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = cadastrarEspecialidades
        fields = ['id', 'nome']

class medicosSeralizer(serializers.ModelSerializer):
    class Meta:
        model = cadastrarMedicos
        fields = ['id', 'CRM', 'nome', 'especialidade']
        depth=1

class consultasSeralizer(serializers.ModelSerializer):
    class Meta:
        model = agendaMedica
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']
        depth=2

class agendarConsultaSeralizer(serializers.ModelSerializer):
    class Meta:
        model = agendaMedica
        fields = ['id', 'horario']

class agendaDisponivelSeralizer(serializers.ModelSerializer):
    class Meta:
        model = agendaDisponivel
        fields = ['id', 'medico', 'dia', 'horarios']
        depth=2