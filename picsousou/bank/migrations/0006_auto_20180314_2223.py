# Generated by Django 2.0.3 on 2018-03-14 22:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_auto_20180314_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 3, 14, 22, 23, 37, 213657, tzinfo=utc), verbose_name='Date'),
        ),
    ]
