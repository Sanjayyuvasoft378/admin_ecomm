# Generated by Django 3.2.13 on 2023-03-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0023_auto_20230307_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]