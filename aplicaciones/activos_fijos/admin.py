from django.contrib import admin
from django.contrib.admin import AdminSite
from aplicaciones.activos_fijos.models import Activo, Departamento, Empleado,Categoria

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('ruc','nombre','apellido','ciudad','direccion','estado',)
    ordering = ('nombre','apellido',)
    search_fields = ('ruc','nombre',)
    list_filter = ('ciudad__nombre','estado',)
admin.site.register(Empleado,EmpleadoAdmin)

class ActivoAdmin(admin.ModelAdmin):
    list_display = ('nombres','categoria','precio','fecha_adquisicion',)
    ordering = ('nombres','categoria',)
    search_fields = ('nombres','categoria',)
    list_filter = ('nombres','categoria','estado',)
admin.site.register(Activo,ActivoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre','estado',)
admin.site.register(Categoria,CategoriaAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre','estado',)
admin.site.register(Departamento,DepartamentoAdmin)

