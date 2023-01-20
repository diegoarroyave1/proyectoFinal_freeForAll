# Generated by Django 4.1.3 on 2022-12-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freeforall', '0004_alter_comentarios_id_evento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='clave',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='rol',
            field=models.CharField(choices=[('A', 'Administrador'), ('S', 'Supervisor'), ('O', 'Operario')], default='O', max_length=100),
        ),
    ]
