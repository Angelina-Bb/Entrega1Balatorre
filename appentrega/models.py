from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    laboratorio = models.CharField(max_length=30)
    codigo = models.IntegerField()
    stock = models.IntegerField()

class Carrito(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad = models.IntegerField()

class Pedido(models.Model):
    factura = models.IntegerField
    cant_prod = models.IntegerField