# Generated by Django 2.1.7 on 2019-04-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190414_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='phone_no',
            field=models.CharField(max_length=32, verbose_name='Phone'),
        ),
    ]
