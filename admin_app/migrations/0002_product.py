# Generated by Django 3.2.13 on 2023-02-23 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('image', models.ImageField(upload_to='product')),
                ('description', models.TextField()),
                ('main_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.maincategory')),
                ('sub_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.subcategory')),
            ],
        ),
    ]