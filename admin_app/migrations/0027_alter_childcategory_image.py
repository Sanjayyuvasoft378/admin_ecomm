# Generated by Django 3.2.13 on 2023-03-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0026_auto_20230309_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childcategory',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
