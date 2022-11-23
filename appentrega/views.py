from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from appentrega.models import *
import os

def inicio(request):
    ruta = os.path.abspath(os.path.curdir)
    ruta_completa = ruta + r'\appentrega\templates\appentrega\index.html'
    archivo = open(ruta_completa)
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def productos(request):
    ruta = os.path.abspath(os.path.curdir)
    ruta_completa = ruta + r'\appentrega\templates\appentrega\productos.html'
    archivo = open(ruta_completa)
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def form_productos(request):
    if request.method == 'GET':
        producto = Producto(request.GET['cliente'], request.GET['email'], request.GET['nombre'], request.GET['droga'], request.GET['laboratorio'], request.GET['codigo'], request.GET['stock'], request.GET['precio'])
        producto.save()
        return render(request, "appentrega/pedidos.html")
    return render(request, )

def carrito(request):
    ruta = os.path.abspath(os.path.curdir)
    ruta_completa = ruta + r'\appentrega\templates\appentrega\carrito.html'
    archivo = open(ruta_completa)
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def pedidos(request):
    ruta = os.path.abspath(os.path.curdir)
    ruta_completa = ruta + r'\appentrega\templates\appentrega\pedidos.html'
    archivo = open(ruta_completa)
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def contacto(request):
    ruta = os.path.abspath(os.path.curdir)
    ruta_completa = ruta + r'\appentrega\templates\appentrega\contacto.html'
    archivo = open(ruta_completa)
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)