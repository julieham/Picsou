# Generated by Django 2.0.3 on 2018-03-14 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
