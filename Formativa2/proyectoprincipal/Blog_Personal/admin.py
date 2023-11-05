from django.contrib import admin
from .models import Post, Categoria, Etiqueta


# Register your models here.
admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Etiqueta)