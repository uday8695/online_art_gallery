# Generated by Django 5.0.6 on 2024-05-31 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artsupplies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artsupplies',
            name='status',
        ),
        migrations.RemoveField(
            model_name='artsupplies',
            name='supplier_name',
        ),
    ]
