# Generated by Django 3.2.13 on 2023-02-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm_app', '0006_alter_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('mobile_no', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
    ]
