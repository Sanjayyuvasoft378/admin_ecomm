# Generated by Django 3.2.13 on 2023-03-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm_app', '0035_delete_uploadimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]