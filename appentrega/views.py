from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse('Bienvenido a la drogueria')
    
def productos(request):
    return HttpResponse('Estas en productos.')

def carrito(request):
    return HttpResponse('Estas en el carrito.')

def pedidos(request):
    return HttpResponse('Estas en pedidos.')

def contacto(request):
    return HttpResponse('Estas en contacto.')