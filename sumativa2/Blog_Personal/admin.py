from django.contrib import admin
from .models import Publicacion, Categoria, Etiqueta


# Register your models here.
admin.site.register(Publicacion)
admin.site.register(Categoria)
admin.site.register(Etiqueta)