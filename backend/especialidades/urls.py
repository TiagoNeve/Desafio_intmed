from django.urls import path
from .views import *

urlpatterns = [
  path('', login_auth, name='login'),
  path('cadastro/', criar_conta, name='criar_conta'),
  path('especialidades/', EspecialidadesList.as_view()),
  path('medicos/', MedicosList.as_view()),
  path('consultas/', ConsultasList.as_view()),
  path('agendas/', agendaDisponivelViewSet.as_view())
]