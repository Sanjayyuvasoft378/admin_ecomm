# Generated by Django 3.2.13 on 2023-02-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm_app', '0008_auto_20230220_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
