# Generated by Django 4.2.7 on 2023-12-30 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0008_image_about_the_center_image_header_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='index',
            field=models.ImageField(blank=True, null=True, upload_to='dynamic_images', verbose_name='Index Image'),
        ),
    ]