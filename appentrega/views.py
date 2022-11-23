from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
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