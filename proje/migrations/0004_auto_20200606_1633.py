# Generated by Django 3.0.5 on 2020-06-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0003_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_slug',
            field=models.SlugField(max_length=120, unique=True, verbose_name='Category Slug'),
        ),
    ]