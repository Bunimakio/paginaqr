from django.shortcuts import render
from django.contrib import admin
from .models import CodigoQr



def qr_image(request):
    img = CodigoQr.objects.all().first()
    return render(request,'qr/imagen.html',{'img':img})