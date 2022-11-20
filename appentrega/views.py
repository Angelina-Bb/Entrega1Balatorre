from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
import os
# Create your views here.

def inicio(request):
    ruta = os.path.abspath(os.path.curdir)
    ruta_completa = ruta + r'\appentrega\templates\index.html'
    archivo = open(ruta_completa)
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def productos(request):
    return HttpResponse('Estas en productos.')

def carrito(request):
    return HttpResponse('Estas en el carrito.')

def pedidos(request):
    return HttpResponse('Estas en pedidos.')

def contacto(request):
    return HttpResponse('Estas en contacto.')