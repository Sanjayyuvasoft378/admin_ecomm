# Generated by Django 3.2.13 on 2023-03-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0024_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
