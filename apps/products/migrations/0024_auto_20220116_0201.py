# Generated by Django 3.2.9 on 2022-01-15 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20220116_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]