# Generated by Django 3.2.13 on 2023-02-21 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm_app', '0021_alter_addtocartmodel_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtocartmodel',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Ecomm_app.product'),
            preserve_default=False,
        ),
    ]