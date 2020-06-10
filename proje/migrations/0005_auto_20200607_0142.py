# Generated by Django 3.0.5 on 2020-06-06 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0004_auto_20200606_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_file',
            field=models.ImageField(upload_to=''),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=120, verbose_name='Comment')),
                ('comment_images', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proje.Images', verbose_name='Comment Image')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
