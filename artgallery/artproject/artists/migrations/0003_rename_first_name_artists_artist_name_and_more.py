# Generated by Django 5.0.6 on 2024-05-30 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_artists_artist_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artists',
            old_name='first_name',
            new_name='artist_name',
        ),
        migrations.RemoveField(
            model_name='artists',
            name='last_name',
        ),
    ]
