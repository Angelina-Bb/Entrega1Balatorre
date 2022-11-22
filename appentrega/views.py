from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
import os
# Create your views here.

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

def carrito(request):
    return HttpResponse('Estas en el carrito.')

def pedidos(request):
    return HttpResponse('Estas en pedidos.')

def contacto(request):
    ruta = os.path.abspath(os.path.curdir)
    ruta_completa = ruta + r'\appentrega\templates\appentrega\contacto.html'
    archivo = open(ruta_completa)
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)