# Generated by Django 2.1.7 on 2019-04-21 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20190421_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Travel Date'),
        ),
    ]
