# Generated by Django 3.2.9 on 2021-11-18 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20211119_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='add_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.addcategory', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='finishes',
            field=models.CharField(blank=True, help_text='<strong style="color:teal">Please seperate the finishes by Bar symbol( | ). Like ex: chrome|brushed-nickel</strong>', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.subcategory', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sup_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.supcategory', unique=True),
        ),
    ]
