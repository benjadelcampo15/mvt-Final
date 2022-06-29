from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name= 'inicio' ),
    
    
    path('usuarios/', usuarios, name='usuarios'),
    path('usuariosCrear/', usuariosCrear, name='usuariosCrear' ),
    path('usuariosBuscar/', usuariosBuscar, name='usuariosBuscar' ),
    
    
    path('posteos/', posteos, name='posteos'),
    path('crearPosteos/' , crearPosteos , name = "crearPosteos"),
    path('buscarPosteos/' , buscarPosteos , name ="buscarPosteos"),

    path('moderadores/', moderadores, name='moderadores'),
    path('crearModeradores/' , creaModeradores , name= 'crearModeradores'  ),
    path('buscarModeradores/' , buscarModeradores , name = 'bucarModeradores'),
]
