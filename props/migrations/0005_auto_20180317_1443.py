# Generated by Django 2.0.3 on 2018-03-17 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('props', '0004_auto_20180317_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prop',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 17, 14, 43, 1, 217279)),
        ),
        migrations.AlterField(
            model_name='prop',
            name='takers',
            field=models.ManyToManyField(blank=True, null=True, to='props.GGMLUser'),
        ),
    ]
