from django.db import models
from django.utils.timezone import now

from aplicaciones.core.models import Base, Pais, Provincia, Ciudad, Grupo, Linea
from proyecto_integrador import settings
from proyecto_integrador.constantes import Opciones
opciones = Opciones()
GENERO = opciones.genero()

class Empleado(Base):
    ruc = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=200, unique=True)
    apellido = models.CharField(max_length=200, unique=True)
    cargo = models.CharField(max_length=200, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')
    genero = models.CharField(max_length=1, choices=GENERO,default=GENERO[0][0], blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100,unique=True)
    foto = models.FileField(upload_to='activos_fijos/empleados/', blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nombre, self.apellido)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ('nombre',)

    def get_image(self):
        if self.foto:
            return '{}{}'.format(settings.MEDIA_URL, self.foto)
        return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')



class Activo(Base):
    nombres = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=200, unique=True)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio del Activo')
    fecha_adquisicion = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nombres)

    class Meta:
        verbose_name = "Activo"
        verbose_name_plural = "Activos"
        ordering = ('nombres',)


class Categoria(models.Model):
    #campos
    nombre = models.CharField(max_length=50, blank=True, null=True)
    estado = models.BooleanField(default=True)

    #definimos las clase meta
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre']
    def _str_(self):
        return self.nombre


#creacion modelo departamento
class Departamento(models.Model):
    #campos
    nombre = models.CharField(max_length=50, blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)
     #definimos las clase meta
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['nombre']
    def _str_(self):
        return self.nombre


