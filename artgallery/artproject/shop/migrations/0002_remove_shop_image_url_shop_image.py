# Generated by Django 5.0.6 on 2024-06-04 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='image_url',
        ),
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
