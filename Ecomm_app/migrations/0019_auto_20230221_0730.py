# Generated by Django 3.2.13 on 2023-02-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm_app', '0018_alter_addtocartmodel_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtocartmodel',
            name='qty',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='qty',
            field=models.IntegerField(),
        ),
    ]