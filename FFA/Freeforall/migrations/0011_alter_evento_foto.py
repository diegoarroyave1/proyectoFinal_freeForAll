# Generated by Django 4.1.3 on 2022-12-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freeforall', '0010_alter_evento_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='foto',
            field=models.ImageField(default='Freeforall/fotos/default.jpg', upload_to='Freeforall/fotos'),
        ),
    ]