# Generated by Django 3.1 on 2020-09-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0016_auto_20200910_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendadisponivel',
            name='horarios',
            field=models.ManyToManyField(null=True, to='especialidades.horariosDisponiveis'),
        ),
    ]
