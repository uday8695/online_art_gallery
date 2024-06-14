# Generated by Django 5.0.6 on 2024-06-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_address_remove_profile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('artist', 'Artist'), ('customer', 'Customer'), ('admin', 'Admin')], max_length=20),
        ),
    ]