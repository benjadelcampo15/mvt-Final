from django.contrib import admin
from .models import *

# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'nacimiento')
    search_fields = ('nombre', 'nacimiento')


admin.site.register(Usuario, UsuarioAdmin)



