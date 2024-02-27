from django.contrib import admin
from .models import Categoria, Panos

class CategoriaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Categoria, CategoriaAdmin)

@admin.register(Panos)
class PanosAdmin(admin.ModelAdmin):
    ...
