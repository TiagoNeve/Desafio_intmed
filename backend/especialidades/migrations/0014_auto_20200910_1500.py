# Generated by Django 3.1 on 2020-09-10 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0013_auto_20200909_0123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendamedica',
            options={'ordering': ['horario'], 'verbose_name_plural': 'Agenda medica'},
        ),
    ]