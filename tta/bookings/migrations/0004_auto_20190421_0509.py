# Generated by Django 2.1.7 on 2019-04-21 05:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20190421_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='seats_booked',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='# of seats booked'),
        ),
        migrations.AlterField(
            model_name='train',
            name='seats_remaining',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='# of seats remaining'),
        ),
    ]
