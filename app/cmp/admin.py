from django.contrib import admin

# Register your models here.
from app.cmp.models import Proveedor,ComprasEnc,ComprasDet



admin.site.register(Proveedor )
admin.site.register(ComprasEnc )
admin.site.register(ComprasDet)
