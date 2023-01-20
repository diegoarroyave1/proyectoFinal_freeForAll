# Generated by Django 4.1.3 on 2022-12-04 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Freeforall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitaciones',
            fields=[
                ('id_invitaciones', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_invitacion', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id_liga', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_liga', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(max_length=20)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fecha_de_nacimiento', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_evento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_evento', models.CharField(max_length=15, unique=True)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('feha_fin', models.DateTimeField(auto_now_add=True)),
                ('ubicacion', models.CharField(max_length=15)),
                ('precio', models.IntegerField()),
                ('Municipio', models.CharField(max_length=15, unique=True)),
                ('id_invitaciones', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Freeforall.invitaciones')),
                ('id_liga', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Freeforall.liga')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Freeforall.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id_comentarios', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Comentarios', models.CharField(max_length=15)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('hora_ingreso', models.DateTimeField(auto_now_add=True)),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Freeforall.evento')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Freeforall.usuarios')),
            ],
        ),
    ]
