# Generated by Django 3.2.13 on 2023-02-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm_app', '0016_auto_20230221_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='qty',
            field=models.CharField(max_length=20),
        ),
    ]
