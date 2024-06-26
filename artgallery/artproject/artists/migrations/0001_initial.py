# Generated by Django 5.0.6 on 2024-05-24 05:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('artist_age', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('experience', models.PositiveIntegerField()),
                ('earnings', models.CharField(max_length=50)),
                ('no_of_drawings_made', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
