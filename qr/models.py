from django.db import models
from django.conf import settings

class CodigoQr(models.Model):
    """ Creo un modelo de CodigoQr cuyo unico atributo es un ImageField """
    
    authorQr = models.CharField(max_length=50)
    titleQr = models.CharField(max_length=100)
    linkQr = models.TextField()
    imgQr = models.ImageField()
