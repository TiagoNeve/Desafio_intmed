# Generated by Django 3.1 on 2020-09-04 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0002_auto_20200904_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrarmedicos',
            name='telefone',
            field=models.PositiveBigIntegerField(blank=True, help_text='(Opcional) Digite um telefone válido'),
        ),
    ]
