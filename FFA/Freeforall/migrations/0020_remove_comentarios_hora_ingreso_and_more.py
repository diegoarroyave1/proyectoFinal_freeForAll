# Generated by Django 4.1.3 on 2022-12-12 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Freeforall', '0019_alter_evento_competidor_alter_evento_espectador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='hora_ingreso',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='competidor',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='espectador',
        ),
    ]
