from django.db import models
from django.conf import settings

class CodigoQr(models.Model):
    imageQr = models.ImageField()

