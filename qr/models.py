from django.db import models
from django.conf import settings

class CodigoQr(models.Model):
    """ Creo un modelo de CodigoQr cuyo unico atributo es un ImageField """
    
    imageQr = models.ImageField()

