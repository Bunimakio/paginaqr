from django.urls import path
from . import views

""" Para mostrar la vista en la pagina se utiliza la funcion qr_image definida en views.py """

urlpatterns = [
    path('',views.qr_login, name='qr_login'),
    path('accounts/login/imagen/', views.qr_image, name='qr_image'),
    path('accounts/logout/home/', views.qr_login, name='qr_image'),
]