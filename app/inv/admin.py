from django.contrib import admin

# Register your models here.
from app.inv.models import Categoria,SubCategoria,Marca,UnidadMedida,Producto



admin.site.register(Categoria )
admin.site.register(SubCategoria )
admin.site.register(Marca)
admin.site.register(UnidadMedida)
admin.site.register(Producto)
