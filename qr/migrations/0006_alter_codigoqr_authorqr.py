# Generated by Django 4.1.7 on 2023-04-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0005_codigoqr_authorqr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigoqr',
            name='authorQr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
