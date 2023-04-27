from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def validar_miembro(request):
    
    return render(request,'member/auth_page.html',{})
