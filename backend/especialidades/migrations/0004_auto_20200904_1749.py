# Generated by Django 3.1 on 2020-09-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0003_auto_20200904_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrarmedicos',
            name='telefone',
            field=models.CharField(max_length=13),
        ),
    ]
