# Generated by Django 3.1 on 2020-09-04 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendamedica',
            options={'verbose_name': 'Agendamento'},
        ),
        migrations.AlterModelOptions(
            name='cadastrarespecialidades',
            options={'verbose_name': 'Especialidade'},
        ),
        migrations.AlterModelOptions(
            name='cadastrarmedicos',
            options={'verbose_name': 'Medico'},
        ),
        migrations.AlterField(
            model_name='agendamedica',
            name='horario',
            field=models.DateTimeField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cadastrarmedicos',
            name='CRM',
            field=models.IntegerField(help_text='Informe o CRM do Médico'),
        ),
        migrations.AlterField(
            model_name='cadastrarmedicos',
            name='email',
            field=models.EmailField(blank=True, help_text='(Opcional) Digite um Email válido', max_length=254),
        ),
        migrations.AlterField(
            model_name='cadastrarmedicos',
            name='especialidade',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.cadastrarespecialidades', verbose_name='Especialidade'),
        ),
        migrations.AlterField(
            model_name='cadastrarmedicos',
            name='nome',
            field=models.CharField(help_text='Nome do médico', max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cadastrarmedicos',
            name='telefone',
            field=models.IntegerField(blank=True, help_text='(Opcional) Digite um telefone válido'),
        ),
    ]