from django.urls import path
from appentrega.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('productos/', productos),
    path('carrito/', carrito),
    path('pedidos/', pedidos),
    path('contacto/', contacto)

]