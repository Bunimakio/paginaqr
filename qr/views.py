from django.shortcuts import render
from django.contrib import admin
from .models import CodigoQr



def qr_image(request):
    
    """ Esta funcion devuelve el primer elemento de un QuerySet que es un objeto imagen,
    esto se almacena en un context con el nombre img"""

    img = CodigoQr.objects.all().first()
    return render(request,'qr/imagen.html',{'img':img})