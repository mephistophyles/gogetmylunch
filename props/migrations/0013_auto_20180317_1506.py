# Generated by Django 2.0.3 on 2018-03-17 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('props', '0012_auto_20180317_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prop',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 17, 15, 6, 0, 79137)),
        ),
    ]
