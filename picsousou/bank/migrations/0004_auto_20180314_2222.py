# Generated by Django 2.0.3 on 2018-03-14 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20180314_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='date',
            field=models.DateField(default=datetime.date(2018, 3, 14), verbose_name='Date'),
        ),
    ]
