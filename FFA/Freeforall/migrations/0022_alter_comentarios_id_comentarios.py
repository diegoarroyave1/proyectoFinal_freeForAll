# Generated by Django 4.1.3 on 2022-12-12 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freeforall', '0021_rename_comentarios_comentarios_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='id_comentarios',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
