# Generated by Django 3.2.13 on 2023-03-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0020_auto_20230303_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
