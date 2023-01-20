from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id_usuario',)
    search_fields = ['id_usuario']


@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id_usuario','primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'fecha_de_nacimiento',"rol")
    search_fields = ['primer_nombre']

   

@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
    list_display = ('id_liga', 'nombre_liga', )
    search_fields = ['nombre_liga']

@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('id_comentarios', 'comentarios', 'id_evento', 'id_usuario', )
    search_fields = ['id_comentarios']


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id_evento', 'nombre_evento', 'fecha_inicio', 'feha_fin', 'precio', 'Municipio','id_usuario','id_liga', 'foto', 'verFoto', 'estado', )
    search_fields = ['nombre_evento']

    def verFoto(self, obj):
        from django.utils.html  import format_html
        return format_html('<img src="{}" width="20%" />'.format(obj.foto.url))

    

@admin.register(Invitaciones)
class InvitacionesAdmin(admin.ModelAdmin):
    list_display = ('id_invitaciones', 'nombre_invitacion', 'email', )
    search_fields = ['nombre_invitacion']  