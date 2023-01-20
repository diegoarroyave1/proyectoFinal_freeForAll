from django.urls import path
from . import views

app_name = "Freeforall"

urlpatterns = [

    path('', views.index, name="index" ),
    path('login/', views.login, name="login" ),
    path('login/nuevo', views.loginFormulario, name="loginFormulario" ),
    path('logout/', views.logout, name="logout" ),
    path('login/register', views.formularioRegister, name="nuevoRegistro" ),
    path('login/nuevo', views.formularioRegister, name="nuevoRegistro" ),

    path('restablecer/',views.restablecer, name="restablecer"),
    path('showRestablecer/',views.showRestablecer, name="showRestablecer"),
    path('restablecerPassword/<id>', views.cambiarPassword, name="restablecerPassword"),
    path('cambiarPws/', views.cambiarPws, name="cambiarPws"),

    path('invitacion/enviar/<id>',views.formInvitacion, name="nuevoInvitacion"),
    path('invitacion/',views.invitacion, name="invitacion"),


    path('usuarios', views.listarUsuarios, name='listarUsuarios'),
    path('usuarios/nuevo', views.formularioUsuario, name='nuevoUsuario'),
    path('usarios/guardar', views.guardarUsuario, name='guardarUsuario'),
    path('usarios/actualizar/<id>', views.editarUsuario, name='editarUsuario'),
    path('usarios/editar', views.actualizarUsuario, name='actualizarUsuario'),

    path('ligas', views.listarLigas, name='listarLigas'),
    path('ligas/nuevo', views.formularioLiga, name='nuevoliga'),
    path('ligas/guardar', views.guardarLiga, name='guardarLiga'),
    path('ligas/eliminar/<id>', views.eliminarLiga, name='eliminarLiga'),
    path('ligas/actualizar/<id>', views.editarLiga, name='editarLiga'),
    path('ligas/editar', views.actualizarLiga, name='actualizarliga'),

    path('eventos', views.listarEventos, name='listarEventos'),
    path('eventos/nuevo', views.formularioEvento, name='nuevoEvento'),
    path('eventos/guardar', views.guardarEvento, name='guardarEvento'),
    path('eventos/eliminar/<id>', views.eliminarEvento, name='eliminarEvento'),
    path('eventos/actualizar/<id>', views.editarEvento, name='editarEvento'),
    path('eventos/editar', views.actualizarEvento, name='actualizarEvento'),
    path('eventos/competidor/<pk>', views.ADDcompetidor, name='competidor'),
    path('eventos/espectador/<pk>', views.ADDespectador, name='espectador'),

    path('comentarios', views.listarComentarios, name='listarComentarios'),
    path('comentarios/nuevo/<id>', views.formularioComentarios, name='nuevoComentarios'),
    path('comentarios/guardar', views.guardarComentarios, name='guardarComentarios'),
    path('comentarios/eliminar/<id>', views.eliminarComentarios, name='eliminarComentarios'),
    path('comentarios/actualizar/<id>', views.editarComentarios, name='editarComentarios'),
    path('comentarios/editar', views.actualizarComentarios, name='actualizarComentarios'),

    path('perfil/<id>', views.perfil, name='perfil'),

]