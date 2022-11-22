from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    droga = models.CharField(max_length=25)
    laboratorio = models.CharField(max_length=30)
    codigo = models.IntegerField()
    stock = models.BooleanField()

class Carrito(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField()
    cantidad = models.IntegerField()

class Pedido(models.Model):
    factura = models.IntegerField()
    cant_prod = models.IntegerField()

class Contacto(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = models.IntegerField()
    email = models.EmailField()
    texto = models.CharField(max_length=500)