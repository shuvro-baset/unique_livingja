# Generated by Django 3.2.9 on 2022-01-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20220116_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
