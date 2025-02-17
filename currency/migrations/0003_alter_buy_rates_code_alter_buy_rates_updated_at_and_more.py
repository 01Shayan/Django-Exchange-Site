# Generated by Django 4.2.10 on 2025-01-27 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_buy_rates_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy_rates',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='buy_rates',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 13, 8, 12, 864934)),
        ),
        migrations.AlterField(
            model_name='sell_rates',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='sell_rates',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 13, 8, 12, 865046)),
        ),
    ]
