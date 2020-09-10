from django.db import models
from datetime import datetime, date
from django.core.exceptions import ValidationError

# Create your models here.
class cadastrarEspecialidades(models.Model):
    nome = models.CharField(max_length=255,
                            verbose_name='Nome')

    class Meta:
        verbose_name = 'Especialidade'

    def __str__(self):
        return self.nome


class cadastrarMedicos(models.Model):
    nome = models.CharField(max_length=255,
                            verbose_name='Nome',
                            help_text='Nome do médico')
    CRM = models.IntegerField(help_text='Informe o CRM do Médico')
    email = models.EmailField(max_length=254,
                              blank=True,
                              help_text='(Opcional) Digite um Email válido')
    telefone = models.CharField(max_length=13,
                                blank=True)
    especialidade = models.ManyToManyField(cadastrarEspecialidades, blank=True, verbose_name='Especialidade')

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Médicos'

    def __str__(self):
        return self.nome

class agendaMedica(models.Model):

    # def authAgenda(self):
    #    for lista in agendaMedica.objects.values_list('agdMedico', 'dataAgenda'):
    #        if self.agdMedico in lista and self.dataAgenda in lista:
    #            return

    def agdPassada(value):
        if value < date.today():
            raise ValidationError(
                'Não pode agendar em dias que passaram'
            )

    medico = models.ForeignKey(cadastrarMedicos,
                                  on_delete=models.PROTECT,
                                  verbose_name='Médico')
    dia = models.DateField(null=True, verbose_name='Data do agendamento', validators=[agdPassada])

    horario = models.TimeField(null=True, blank=True, verbose_name='Horário do agendamento')

    data_agendamento = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}, {}'.format(self.medico, self.dia)

    class Meta:
        ordering = ['horario']
        verbose_name_plural = 'Agenda medica'
        unique_together = (('medico', 'dia'))


class horariosDisponiveis(models.Model):
    horarios = models.TimeField()

    def __str__(self):
        return '{}'.format(self.horarios)


# Verificar depois -> Agenda disponíveis
class agendaDisponivel(models.Model):

    def agdPassada(value):
        if value < date.today():
            raise ValidationError(
                'Não pode agendar em dias que passaram'
            )

    medico = models.ForeignKey(cadastrarMedicos,
                                   on_delete=models.PROTECT,)
    dia = models.DateField('Dias disponíveis', validators=[agdPassada])
    horarios = models.ManyToManyField(horariosDisponiveis, null=True)

    class Meta:
        unique_together = (('medico', 'dia'))
        ordering = ['dia']


    def __str__(self):
        return '{}, {}'.format(self.medico, self.dia)

class Contas(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=255)

