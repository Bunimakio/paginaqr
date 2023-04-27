from django import forms
from django.forms import HiddenInput
from .models import CodigoQr

class QrForms(forms.ModelForm):
    class Meta():
        model = CodigoQr
        fields = ["titleQr","linkQr"]
