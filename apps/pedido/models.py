from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    rol      = models.ManyToManyField(Rol)
    alias    = models.CharField(max_length=50)

class TipoComponente(models.Model):
    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(max_length=200, blank=False, null=False)        
    
    def __str__(self):
        return self.descripcion

class Componente(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200, blank=False, null=False)        
    id_tipo = models.ForeignKey(TipoComponente,on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='pictures', max_length=255, null=True, blank=True)   
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion

class Orden(models.Model):
    id = models.AutoField(primary_key=True)
    Numero = models.IntegerField()
    descripcion = models.CharField(max_length=200, blank=False, null=False)        
    fecha = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)
    cliente = models.CharField(max_length=200, blank=False, null=False)        
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
        ordering = ['fecha']

    def __str__(self):
        return self.descripcion

class DetalleOrden(models.Model):
    id = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Orden,on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Componente,on_delete=models.CASCADE)
    idGrupo = models.IntegerField()
    cantidad = models.IntegerField()
    
    class Meta:
        verbose_name = 'DetalleOrden'
        verbose_name_plural = 'DetalleOrdenes'
        ordering = ['id']
