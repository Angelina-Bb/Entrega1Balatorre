from django.urls import path
from appentrega import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('productos/', views.productos, name="Productos"),
    path('carrito/', views.carrito, name="Carrito"),
    path('pedidos/', views.pedidos, name="Pedidos"),
    path('contacto/', views.contacto, name="Contacto")

]