from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('nombre', 'descripcion')

#admin.site.register(Band)  # Use the default options
admin.site.register(Categoria, CategoriaAdmin)  	