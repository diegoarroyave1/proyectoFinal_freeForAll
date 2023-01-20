# Generated by Django 4.1.3 on 2022-12-04 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Freeforall.genero')),
            ],
            options={
                'db_table': 'Libros',
            },
        ),
    ]
