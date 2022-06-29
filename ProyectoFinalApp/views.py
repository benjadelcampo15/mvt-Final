








from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.

# Inicio
def inicio(request):
    
    return render(request,'index.html')

def redirec(request):
    return render(request, 'redirec.html')


# Usuarios
def usuarios(request):
    
    usuarios = Usuario.objects.all()
    
    return render(request,'usuarios.html', {'usuarios':usuarios})



def usuariosCrear(request):
        # post
    if request.method == "POST":
        
        formulario = usuarioCrear(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            usuario = Usuario(nombre=info["nombre"],mail=info["mail"],nacimiento=info["nacimiento"])
            usuario.save()

            return redirect("usuariosCrear")

        return render(request,"usuariosCrear.html",{"form":formulario})

    # get
    formulario = usuarioCrear()
    return render(request,"usuariosCrear.html",{"form":formulario})


def usuariosBuscar(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            usuarios = Usuario.objects.filter( Q(nombre__icontains=search) | Q(nacimiento__icontains=search) ).values()

            return render(request,"usuariosBuscar.html",{"usuarios":usuarios, "search":True, "busqueda":search})

        else:
        
            usuarios = Usuario.objects.all()

            return render(request,"usuariosBuscar.html",{"usuarios":usuarios, "search":False})
    
    else:
        
        usuarios = Usuario.objects.all()

        return render(request,"usuariosBuscar.html",{"usuarios":usuarios, "search":False})



# Posteos

def posteos(request):
    
     posteos = Posteo.objects.all()
    
     return render(request,'posteos.html', {'posteos':posteos})

def crearPosteos(request):
     if request.method == "POST":
        
        formulario = posteoCrear(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            posteo = Posteo(titulo=info["titulo"],cuerpo=info["cuerpo"])
            posteo.save()

            return redirect("crearPosteos")

        return render(request,"crearPosteos.html",{"form":formulario})

    # get
     formulario = posteoCrear()
     return render(request,"crearPosteos.html",{"form":formulario})

def buscarPosteos(request):
     if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            posteos = Posteo.objects.filter( Q(titulo__icontains=search) | Q(cuerpo__icontains=search) ).values()

            return render(request,"buscarPosteos.html",{"posteos":posteos, "search":True, "busqueda":search})

        else:
        
            posteos = Posteo.objects.all()

            return render(request,"buscarPosteos.html",{"posteos":posteos, "search":False})
    
     else:
        
        posteos = Posteo.objects.all()

        return render(request,"buscarPosteos.html",{"posteos":posteos, "search":False})


# Moderadores

def moderadores(request):
    
    moderadores = Moderador.objects.all()
    
    return render(request,'moderadores.html', {'moderadores':moderadores})

def creaModeradores(request):
    
     if request.method == "POST":
        
        formulario = moderadorCrear(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            moderador = Moderador(nombre=info["nombre"],mail=info["mail"],sector=info["sector"])
            moderador.save()

            return redirect("crearModeradores")

        return render(request,"crearModeradoderes.html",{"form":formulario})

    # get
     formulario = usuarioCrear()
     return render(request,"crearModeradores.html",{"form":formulario})
def buscarModeradores(request):
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            moderadores = Moderador.objects.filter( Q(titulo__icontains=search) | Q(cuerpo__icontains=search) ).values()

            return render(request,"buscarModeradores.html",{"moderadores":moderadores, "search":True, "busqueda":search})

        else:
        
            moderadores = Posteo.objects.all()

            return render(request,"buscarModeradores.html",{"moderadores":moderadores, "search":False})
    
    else:
        
         moderadores = Posteo.objects.all()

         return render(request,"buscarModeradores.html",{"moderadores":moderadores, "search":False})

