# Generated by Django 3.0.5 on 2020-06-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0008_auto_20200608_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_file',
            field=models.ImageField(upload_to=''),
        ),
    ]