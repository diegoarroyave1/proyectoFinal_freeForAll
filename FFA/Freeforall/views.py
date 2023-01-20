from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
# Create your views here.
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

from os import remove, path
def index(request):
    return render(request, 'Freeforall/index.html')

"""Login"""
def loginFormulario(request):
    """Redirecciona al formulario del login

    Returns:
        template:`Freeforall/login/login.html`
    
    """
    return render(request, 'Freeforall/login/login.html')

def login(request):
    """Se usa para validar el email y la clave y dar los permisos dependiendo el rol (A),(E),(C)

    Arg:
    login: Optiene los datos para la sesion

    Returns:
        template:`Freeforall:listarEventos`
    
    """
    if request.method == "POST":
        try:
            mail = request.POST["email"]
            passw = request.POST["clave"]

            usuarios = Usuarios.objects.get(email = mail, clave = passw)
            # crear la sesión
            request.session["logueo"] = [usuarios.primer_nombre,usuarios.primer_apellido, usuarios.rol, usuarios.id_usuario, usuarios.get_rol_display()]
            # ----------------------------
            messages.success(request, "Bienvenido!!")
            return redirect('Freeforall:listarEventos')     

        except Usuarios.DoesNotExist:
            messages.error(request, "Usuario no Existe")
            return redirect('Freeforall:loginFormulario')
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('Freeforall:loginFormulario')
    else:
        return redirect('Freeforall:loginFormulario')

def logout(request):
    """Se usa para validar el email y la clave y dar los permisos dependiendo el rol (A),(E)


        Returns:
            template:`Freeforall:loginFormulario`
    """

    try:
        del request.session["logueo"]
        messages.success(request, "Sesión cerrada correctamente!!")
        return redirect('Freeforall:index')
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return redirect('Freeforall:index')

def formularioRegister(request):
    """Redirecciona al formulario del Register

    Returns:
        template:`Freeforall/login/register.html`
    
    """
    return render(request, 'Freeforall/login/register.html')        
 
"""Usuarios"""

def listarUsuarios(request):
    """Se usa para listar los usuarios existentes

    Returns:
        template:`Freeforall/usuarios/usuarios.html`
    
    """
    usuarios = Usuarios.objects.all()
    return render(request, 'Freeforall/usuarios/usuarios.html', {"usuarios":  usuarios})   

def formularioUsuario(request):
    """Redirecciona al formulario del Usuario

    Returns:
        template:`Freeforall/usuarios/nuevo.html`
    
    """
    return render(request, 'Freeforall/login/register.html')

def guardarUsuario(request):
    """Se usa para guardar un usuario

    Arg:
    Usuario: Optiene los datos para registrar los usuarios,('id_usuario', 'estado', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'fecha_de_nacimiento', 'clave', 'ROLES', 'rol', )

    Returns:
        template:`Freeforall:listarEventos`
    """

    try:
        usuario = Usuarios( 
            primer_nombre = request.POST["primer_nombre"],
            segundo_nombre = request.POST["segundo_nombre"],
            primer_apellido = request.POST["primer_apellido"],
            segundo_apellido = request.POST["segundo_apellido"],
            email = request.POST["email"],
            fecha_de_nacimiento = request.POST["fecha_de_nacimiento"],
            clave = request.POST["clave"],
            rol = request.POST["rol"],
        )
        usuario.save()
        messages.success(request, "Usuario guardado correctamente!!")
    except:
        messages.error(request, "Usuario no tiene los datos nesesarios")
        return render(request, 'Freeforall/login/register.html')

    return redirect('Freeforall:listarEventos')

def editarUsuario(request, id):
    """Redirecciona al formulario editar Usuario

    Returns:
        template:`Freeforall/usuarios/actualizar.html`
    """

    usuarios = Usuarios.objects.get(id_usuario = id)
    return render(request, 'Freeforall/usuarios/actualizar.html', {"usuarios": usuarios})

def actualizarUsuario(request):
    """Se usa para actualizar un usuario

    Arg:
    Usuario: Optiene los datos para actualizar los usuarios,('id_usuario', 'estado', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'fecha_de_nacimiento', 'clave', 'ROLES', 'rol', )

    Returns:
        template:`Freeforall/usuarios/actualizar.html`
    """
    try:
        usuarios = Usuarios.objects.get(id_usuario = request.POST["id_usuario"])
        usuarios.primer_nombre = request.POST["primer_nombre"]
        usuarios.segundo_nombre = request.POST["segundo_nombre"]
        usuarios.primer_apellido = request.POST["primer_apellido"]
        usuarios.segundo_apellido = request.POST["segundo_apellido"]
        usuarios.email = request.POST["email"]
        usuarios.fecha_de_nacimiento = request.POST["fecha_de_nacimiento"]
        usuarios.clave = request.POST["clave"]
        usuarios.rol = request.POST["rol"]
        usuarios.save()
        messages.success(request, "Usuario actualizado correctamente")
    except:
        messages.error(request, "Usuario actualizado correctamente")
        return redirect('Freeforall:editarUsuario')


    return redirect('Freeforall:listarUsuarios')

"""Ligas"""


def listarLigas(request):
    """Se usa para listar las ligas existentes

    Returns:
        template:`Freeforall/ligas/ligas.html`
    
    """
    ligas = Liga.objects.all()
    return render(request, 'Freeforall/ligas/ligas.html', {"ligas":  ligas})   

def formularioLiga(request):
    """Redirecciona al formulario de liga

    Returns:
        template:`Freeforall/ligas/nuevo.html`
    
    """
    return render(request, 'Freeforall/ligas/nuevo.html')

def guardarLiga(request):
    """Se usa para guardar una liga

    Arg:
    Usuario: Optiene los datos para registrar las ligas,('id_liga', 'nombre_liga', )

    Returns:
        template:`Freeforall:listarLigas`
    """
    try:
        if request.method == "POST":
            liga = Liga( 
                nombre_liga = request.POST["nombre_liga"],
            )
            liga.save()
            messages.success(request, "Producto guardado correctamente!!")
        else:
            messages.warning(request, "Usted no ha enviado datos...")
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return render(request, 'Freeforall/ligas/nuevo.html')

    return redirect('Freeforall:listarLigas')

def formularioEditarLiga(request):
    """Redirecciona al formulario del Usuario

    Returns:
        template:`Freeforall/ligas/actualizar.html'`
    
    """
    return render(request, 'Freeforall/ligas/actualizar.html')    

def eliminarLiga(request, id):
    """Se usa para eliminar una liga

    Arg:
    Usuario: Optiene el id  eliminar una liga

    Returns:
        template:`Freeforall:listarLigas`
    """
    try:
        liga = Liga.objects.get(id_liga = id)
        liga.delete()
        pass
    except Exception as e:
        messages.error(request, f"Error: {e}")
    return redirect('Freeforall:listarLigas')

def editarLiga(request, id):
    """Redirecciona al formulario editar Liga

    Returns:
        template:`Freeforall/ligas/actualizar.html`
    """
    liga = Liga.objects.get(id_liga = id)
    return render(request, 'Freeforall/ligas/actualizar.html', {"liga": liga})

def actualizarLiga(request):

    """Se usa para actualizar un usuario

    Arg:
    Usuario: Optiene los datos para actualizar los usuarios,('id_liga', 'nombre_liga', )

    Returns:
        template:`Freeforall/usuarios/actualizar.html`
    """
    try:
        liga = Liga.objects.get(id_liga = request.POST["id_liga"])
        liga.nombre_liga = request.POST["nombre_liga"],
        liga.save()
        messages.success(request, "Liga Actualizada correctamente!!")
    except Exception as e:
        messages.error(request, f"Error: {e}")
        messages.error(request, "Liga no se puedo actualizar!!")

    return redirect('Freeforall:listarLigas') 

#Eventos   


def listarEventos(request):
    """Se usa para listar los eventos existentes

    Returns:
        template:`Freeforall/eventos/eventos.html`
    
    """
    comentarios = Comentarios.objects.all()
    eventos = Evento.objects.all().order_by('-id_evento')
    return render(request, 'Freeforall/eventos/eventos.html',{"eventos":  eventos, "comentarios":  comentarios})
    
def formularioEvento(request):
    """Redirecciona al formulario de evento

    Returns:
        template:`Freeforall/evento/nuevo.html`
    
    """
    ligas = Liga.objects.all()
    usuarios = Usuarios.objects.all()
    return render(request, 'Freeforall/eventos/nuevo.html', {"ligas":  ligas, "usuarios":  usuarios})

def guardarEvento(request):
    """Se usa para guardar un evento

    Arg:
    Usuario: Optiene los datos para registrar los eventos,('id_liga', 'nombre_liga', )
    ('id_evento', 'nombre_evento', 'fecha_inicio', 'feha_fin', 'ubicacion', 'precio', 'Municipio', 'id_usuario', 'id_liga', 'foto', )

    Returns:
        template:`Freeforall:listarEventos`
    """
    try:
        if request.method == "POST":
            if request.FILES:
                fss = FileSystemStorage()
                f = request.FILES["foto"]
                file = fss.save("Freeforall/fotos/" + f.name, f)
            else:
                file = 'Freeforall/fotos/default.jpg'

            ligas = Liga.objects.get(pk = request.POST["ligas"])
            usuarios = Usuarios.objects.get(pk = request.POST["usuarios"])
            eventos = Evento(
                nombre_evento =  request.POST["nombre_evento"],
                fecha_inicio =   request.POST["fecha_inicio"],
                feha_fin =   request.POST["feha_fin"],
                ubicacion =  request.POST["ubicacion"],
                precio =  request.POST["precio"],
                Municipio =  request.POST["Municipio"],
                id_usuario = usuarios,
                id_liga = ligas,
                foto = file
            )
            eventos.save()
            messages.success(request, " Evento guardado correctamente!!")
            return redirect('Freeforall:listarEventos') 
        else:
            messages.warning(request, "Usted no ha enviado datos...")
            return redirect('Freeforall:nuevoEvento') 
    except Exception as e:
        messages.error(request, f"Error: {e}")

    

def eliminarEvento(request, id):
    """Se usa para eliminar una evento

    Arg:
    Usuario: Optiene el id  eliminar un evento

    Returns:
        template:`Freeforall:listarEventos`
    """
    try:
        evento = Evento.objects.get(id_evento = id)
        evento.delete()
        pass
    except Exception as e:
        messages.error(request, f"Error: {e}")
    return redirect('Freeforall:listarEventos')

def editarEvento(request, id):
    """Redirecciona al formulario editar evento

    Returns:
        template:`Freeforall/eventos/actualizar.html`
    """
    evento = Evento.objects.get(id_evento = id)
    ligas = Liga.objects.all()
    usuarios = Usuarios.objects.all()
    return render(request, 'Freeforall/eventos/actualizar.html', {"evento": evento, "ligas": ligas, "usuarios": usuarios})

def actualizarEvento(request):
    """Se usa para actualizar un evento

    Arg:
    Usuario: Optiene los datos para actualizar un evento,('id_liga', 'nombre_liga', )
    ('id_evento', 'nombre_evento', 'fecha_inicio', 'feha_fin', 'ubicacion', 'precio', 'Municipio', 'id_usuario', 'id_liga', 'foto', )

    Returns:
        template:`Freeforall:listarEventos`
    """
    try:
        ligas = Liga.objects.get(pk = request.POST["ligas"])
        usuarios = Usuarios.objects.get(pk = request.POST["usuarios"])
        evento = Evento.objects.get(id_evento = request.POST["id_evento"])
        evento.nombre_evento = request.POST["nombre_evento"]
        evento.fecha_inicio = request.POST["fecha_inicio"]
        evento.feha_fin = request.POST["feha_fin"]
        evento.ubicacion = request.POST["ubicacion"]
        evento.precio = request.POST["precio"]
        evento.Municipio = request.POST["Municipio"]
        evento.id_usuario = usuarios
        evento.id_liga = ligas
        evento.foto = request.POST["file"]
        evento.save()
    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('Freeforall:listarEventos') 


def showRestablecer(request):
    return render(request, 'restablecer.html')

def cambiarPassword(request, id):
    usuarios = Usuarios.objects.get(id_usuario = id)
    return render(request, 'showRestablecer.html',{"usuarios": usuarios})

def cambiarPws(request):
    try :
        if request.method=="POST":
            usuarios = Usuarios.objects.get(id_usuario = request.POST["id_usuario"])
            usuarios.clave = request.POST["clave"] 
            usuarios.save()
            messages.success(request,"Cambió de contraseña correctamente!")
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
        messages.warning(request,"no se logro cambiar la contraseña")
           
    return render(request, 'Freeforall/login/login.html')

def restablecer(request):
    from django.core.mail import send_mail
    try: 
        if request.method=="POST":
            correoR = request.POST["email"]
            print(correoR)
            us = Usuarios.objects.get(email = correoR)
            print(us.clave)
            send_mail(
                'Mensaje de Freeforall:',
                'Restablezca su contraseña en el siguiente enlace:\n'+
                'http://127.0.0.1:8000/Freeforall/restablecerPassword/'+str(us.pk),
                'dfarroyave1@misena.edu.co',
                [correoR],
                fail_silently=False,
        )
        messages.info(request,'correo enviado')
        return render(request, 'Freeforall/login/login.html')
    except Exception as e: 
        messages.error(request,f"ERROR:{e}")
        messages.error(request,'correo no se puedo enviar')

    return render(request,'index.html')

def formInvitacion(request, id):
    usuarios = Usuarios.objects.get(id_usuario = id)
    return render(request, 'invitacion.html',{"usuarios": usuarios})

def invitacion(request):
    from django.core.mail import send_mail
    try: 
        if request.method=="POST":
            correoR = request.POST["email"]
            print(correoR)
            us = Usuarios.objects.get(email = correoR)
            print(us.clave)
            send_mail(
                'Mensaje de Freeforall:',
                'Hay un evento nuevo que te puede interesar:\n'+
                'http://127.0.0.1:8000/Freeforall/eventos',
                'dfarroyave1@misena.edu.co',
                [correoR],
                fail_silently=False,
        )
        messages.info(request,'correo enviado')
        return render(request, 'Freeforall/eventos/eventos.html')
    except Exception as e: 
        messages.error(request,f"ERROR:{e}")
        messages.error(request,'correo no se puedo enviar')

    return render(request, 'Freeforall/eventos/eventos.html')

def ADDcompetidor(request, pk):
    evento = get_object_or_404(Evento, id_evento=pk)
    if request.user in evento.competidor.all():
        evento.competidor.remove(request.user)
    else:
        evento.competidor.add(request.user)
    return redirect('Freeforall:listarEventos')

def ADDespectador(request, pk):
    evento = get_object_or_404(Evento, id_evento=pk)
    if request.user in evento.espectador.all():
        evento.espectador.remove(request.user)
    else:
        evento.espectador.add(request.user)
    return redirect('Freeforall:listarEventos')




def listarComentarios(request):
    """Se usa para listar los comentarios existentes

    Returns:
        template:`Freeforall/comentarios/comentarios.html`
    
    """
    comentarios = Comentarios.objects.all()
    return render(request, 'Freeforall/comentarios/comentarios.html', {"comentarios":  comentarios})   

def formularioComentarios(request, id):
    """Redirecciona al formulario de comentarios

    Returns:
        template:`Freeforall/comentarios/nuevo.html`
    
    """
    eventos = Evento.objects.get(id_evento = id)
    usuarios = Usuarios.objects.all()
    return render(request, 'Freeforall/comentarios/nuevo.html', {"eventos":  eventos, "usuarios":  usuarios})

def guardarComentarios(request):
    """Se usa para guardar un comentarios

    Arg:
    Usuario: Optiene los datos para registrar los comentarios,('id_liga', 'nombre_liga', )

    Returns:
        template:`Freeforall:listarComentarios`
    """
    try:
        if request.method == "POST":
            eventos = Evento.objects.get(pk = request.POST["eventos"])
            usuarios = Usuarios.objects.get(pk = request.POST["usuarios"])
            comentarios = Comentarios( 
                comentarios = request.POST["comentarios"],
                id_usuario = usuarios,
                id_evento = eventos,

            )
            comentarios.save()
            messages.success(request, "Comentario guardado correctamente!!")
        else:
            messages.warning(request, "Usted no ha enviado datos...")
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return render(request, 'Freeforall/comentarios/nuevo.html')

    return redirect('Freeforall:listarEventos') 

def formularioEditarComentarios(request):
    """Redirecciona al formulario del Usuario

    Returns:
        template:`Freeforall/comentarios/actualizar.html'`
    
    """
    return render(request, 'Freeforall/comentarios/actualizar.html')    

def eliminarComentarios(request, id):
    """Se usa para eliminar una liga

    Arg:
    Usuario: Optiene el id  eliminar una liga

    Returns:
        template:`Freeforall:listarLigas`
    """
    try:
        comentarios = Comentarios.objects.get(id_comentarios = id)
        comentarios.delete()
        pass
    except Exception as e:
        messages.error(request, f"Error: {e}")
    return redirect('Freeforall:listarEventos') 

def editarComentarios(request, id):
    """Redirecciona al formulario editar Liga

    Returns:
        template:`Freeforall/comentarios/actualizar.html`
    """
    
    comentarios = Comentarios.objects.get(id_comentarios = id)
    eventos = Evento.objects.all()
    usuarios = Usuarios.objects.all()
    return render(request, 'Freeforall/comentarios/actualizar.html', {"comentarios": comentarios, "eventos":  eventos, "usuarios":  usuarios})

def actualizarComentarios(request):

    """Se usa para actualizar un comentarios

    Arg:
    Usuario: Optiene los datos para actualizar los comentarios,('id_liga', 'nombre_liga', )

    Returns:
        template:`Freeforall/comentarios/actualizar.html`
    """
    try:
        eventos = Evento.objects.get(pk = request.POST["eventos"])
        usuarios = Usuarios.objects.get(pk = request.POST["usuarios"])
        comentarios = Comentarios.objects.get(id_comentarios = request.POST["id_comentarios"])
        comentarios.comentarios = request.POST["comentarios"]
        usuarios.id_usuario = usuarios
        eventos.id_evento = usuarios
        comentarios.save()
        messages.success(request, "Comentario Actualizado correctamente!!")
    except Exception as e:
        messages.error(request, f"Error: {e}")
        messages.error(request, "Comentario no se puedo actualizar!!")

    return redirect('Freeforall:listarEventos') 

def perfil(request, id,):
    """Se usa para listar los usuarios existentes

    Returns:
        template:`Freeforall/usuarios/usuarios.html`
    
    """
    comentarios = Comentarios.objects.all()
    eventos = Evento.objects.all()
    usuarios = Usuarios.objects.get(id_usuario = id)
    return render(request, 'Freeforall/perfil/perfil.html', {"usuarios":  usuarios, "eventos":  eventos, "comentarios":  comentarios})