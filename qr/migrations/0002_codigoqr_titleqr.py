# Generated by Django 4.1.7 on 2023-04-22 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codigoqr',
            name='titleQr',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
