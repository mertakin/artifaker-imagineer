# Generated by Django 3.0.5 on 2020-06-08 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0005_auto_20200607_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=10000000, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image_category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='proje.Categories', verbose_name='Images Category'),
        ),
    ]