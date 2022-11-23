from django.db import models

# Create your models here.
class Producto(models.Model):
    cliente = models.CharField(max_length=25)
    email = models.EmailField()
    nombre = models.CharField(max_length=30)
    droga = models.CharField(max_length=25)
    laboratorio = models.CharField(max_length=30)
    codigo = models.IntegerField()
    stock = models.BooleanField()
    precio = models.IntegerField()


class Carrito(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

class Pedido(models.Model):
    factura = models.IntegerField()
    tipo = models.CharField(max_length=25)
    cant_prod = models.IntegerField()
    total = models.IntegerField()

class Contacto(models.Model):
    cliente = models.CharField(max_length=25)
    telefono = models.IntegerField()
    email = models.EmailField()
    motivo = models.CharField(max_length=25)
    texto = models.CharField(max_length=500)