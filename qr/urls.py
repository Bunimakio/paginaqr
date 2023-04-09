from django.urls import path
from . import views

urlpatterns = [
    path('', views.qr_image, name='qr_image'),
]