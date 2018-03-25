# Generated by Django 2.0.1 on 2018-03-19 15:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20180319_1502'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Budget',
        ),
        migrations.AddField(
            model_name='operation',
            name='budget',
            field=models.CharField(choices=[('RE', 'Restos'), ('MA', 'Market'), ('CH', 'Charges'), ('HB', 'Hors Budget')], default='HB', max_length=2),
        ),
        migrations.AlterField(
            model_name='operation',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 3, 19, 15, 5, 51, 874001, tzinfo=utc), verbose_name='Date'),
        ),
    ]