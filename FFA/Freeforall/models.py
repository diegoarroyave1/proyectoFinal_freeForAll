from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Login(models.Model):
    id_usuario = models.CharField(max_length=50, blank=False, null=False)


    def __str__(self):
        return f"{self.id_usuario} - {self.id_usuario}"

class Usuarios(models.Model):
    """Esta modelo recibe los datos de los usuarios"""
    id_usuario = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=20, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=20, blank=False, null=False)
    primer_apellido =models.CharField(max_length=20, blank=False, null=False)
    segundo_apellido = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField( blank=False, null=False, unique=True)
    fecha_de_nacimiento = models.DateTimeField()
    clave = models.CharField(max_length=254)
    ROLES = (
        ('A', 'Administrador'),
        ('E', 'Espectador'),
        ('C', 'Creador'),
    )
    rol = models.CharField(max_length=100, choices=ROLES, default='O')
    ESTADOS = (
        ('A', 'Activado'),
        ('D', 'Desactivado'),
        
    )
    estado = models.CharField(max_length=100,  choices=ESTADOS, default='Activado')
    
    
    

    def __str__(self):
        return f"{self.primer_nombre}"

class Invitaciones(models.Model):
    """Esta modelo recibe los datos de las invitaciones"""
    id_invitaciones = models.AutoField(primary_key=True) 
    nombre_invitacion = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField( blank=False, null=False, unique=True)
    
    def __str__(self):
        return f"{self.id_invitaciones}"

class Liga(models.Model):
    """Esta modelo recibe los datos de las ligas"""
    id_liga = models.AutoField(primary_key=True) 
    nombre_liga = models.CharField(max_length=20, blank=False, null=False, unique=True)

    
    def __str__(self):
        return f"{self.nombre_liga}"

class Evento(models.Model):
    """Esta modelo recibe los datos de los Eventos"""
    id_evento = models.AutoField(primary_key=True)
    nombre_evento = models.CharField(max_length=15, blank=False, null=False, unique=True)
    fecha_inicio =  models.DateTimeField()
    feha_fin =  models.DateTimeField()
    ubicacion = models.CharField(max_length=15, blank=False, null=False)
    precio = models.IntegerField(null=False, blank=False)
    Municipio= models.CharField(max_length=15, blank=False, null=False)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True)
    id_liga = models.ForeignKey(Liga, on_delete=models.DO_NOTHING, null=True, blank=True)
    foto = models.ImageField(upload_to = 'Freeforall/fotos', default='Freeforall/fotos/default.webp')
    ESTADOS = (
        ('A', 'Activado'),
        ('D', 'Desactivado'),
        
    )
    estado = models.CharField(max_length=100,  choices=ESTADOS, default='Activado')
    def __str__(self):
        return f"{self.id_evento}"



class Comentarios(models.Model):
    """Esta modelo recibe los datos de los comentarios"""
    id_comentarios =  models.AutoField(primary_key=True)
    comentarios = models.CharField(max_length=15, blank=False, null=False)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"{self.id_comentarios} - {self.comentarios}"
