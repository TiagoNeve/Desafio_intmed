# Generated by Django 3.1 on 2020-09-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0008_auto_20200905_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='agendamedica',
            options={'ordering': ['dataAgenda'], 'verbose_name_plural': 'Agenda medica'},
        ),
    ]
