from django.shortcuts import render,redirect
from django.contrib import admin
from django.contrib.auth.models import User
from .models import CodigoQr
from django.contrib.auth.decorators import login_required
from .forms import QrForms
from .image_treatment import create_image_qr

def qr_login(request):

    return render(request,'home.html',{})

@login_required
def qr_image(request):
    
    """ Esta funcion devuelve el primer elemento de un QuerySet que es un objeto imagen,
    esto se almacena en un context con el nombre img"""

    img = CodigoQr.objects.filter(authorQr=request.user.username)
    return render(request,'imagen.html',{'img':img})

@login_required
def qr_add(request):
    
    form = QrForms()
    if request.method == "POST":

        img_qr_url = create_image_qr(request)

        form_aux = form.save(commit=False)
        form_aux.authorQr = request.user.username
        form_aux.imgQr = img_qr_url
        form_aux.save()

        form = QrForms(request.POST,instance=form_aux)

        if form.is_valid():
            form.save()

    return render(request,'carga_de_QR.html',context = {'form':form})

