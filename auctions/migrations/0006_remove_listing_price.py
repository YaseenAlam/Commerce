# Generated by Django 5.1 on 2024-09-06 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_listing_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='price',
        ),
    ]
