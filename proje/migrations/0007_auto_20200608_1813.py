# Generated by Django 3.0.5 on 2020-06-08 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0006_auto_20200608_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proje.Categories', verbose_name='Images Category'),
        ),
    ]
