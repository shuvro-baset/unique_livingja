# Generated by Django 3.2.9 on 2021-11-18 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20211119_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcategory',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='supcategory',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
