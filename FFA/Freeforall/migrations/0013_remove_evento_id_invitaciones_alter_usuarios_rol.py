# Generated by Django 4.1.3 on 2022-12-12 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freeforall', '0012_remove_libro_genero_delete_genero_delete_libro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='id_invitaciones',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='rol',
            field=models.CharField(choices=[('A', 'Administrador'), ('E', 'Espectador'), ('C', 'Creador')], default='O', max_length=100),
        ),
    ]
