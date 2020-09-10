from datetime import time

from django.forms import ModelForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
import django_filters
from django_filters import rest_framework as filter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, filters

from .models import *
from .serializers import *

#class EspecialidadeFiltro(filters.FilterSet):
#    class Meta:
#        model = cadastrarEspecialidades
#        fields = ['nome',]

class EspecialidadesList(generics.ListAPIView):
    queryset = cadastrarEspecialidades.objects.all()
    serializer_class = especialidadesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

class MedicosList(generics.ListAPIView):
    queryset = cadastrarMedicos.objects.all()
    serializer_class = medicosSeralizer
    filter_backends = [filter.DjangoFilterBackend,]
    filterset_fields = ['nome', 'especialidade']



class ConsultasList(generics.ListAPIView):
    queryset = agendaMedica.objects.exclude(dia__lt=date.today())
    serializer_class = consultasSeralizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

    def post(self, request):
        try:
            serializer = agendarConsultaSeralizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({ 'mensagem': 'Ocorreu um erro no servidor' },
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class agendaDisponivelViewSet(generics.ListAPIView):
    queryset = agendaDisponivel.objects.exclude(dia__lt=date.today())
    serializer_class = agendaDisponivelSeralizer
    filter_backends = [filter.DjangoFilterBackend,]
    filterset_fields = ['medico',]


#class EspecialidadesList(APIView):
#    def get(self, request):
#        try:
#            lista_especialidades = cadastrarEspecialidades.objects.all()
#            serializer = especialidadesSerializer(lista_especialidades, many=True)
#            return Response(serializer.data)
#        except Exception:
#            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
#                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContaForm(ModelForm):
    class Meta:
        model = Contas
        fields = ['nome', 'email', 'senha']


def login_auth(request, template_name='login.html'):
    return render(request, template_name)

def criar_conta(request, template_name='criar_conta.html'):
    form = ContaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, template_name, {'form': form})