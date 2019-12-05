from django.contrib import admin
from .models import Componente,Rol,TipoComponente,Usuario,Orden,DetalleOrden

# Register your models here.
admin.site.register(Componente)
admin.site.register(Rol)
admin.site.register(TipoComponente)
admin.site.register(Usuario)
admin.site.register(Orden)
admin.site.register(DetalleOrden)