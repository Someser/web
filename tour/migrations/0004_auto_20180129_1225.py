# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_trip_trip_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='no_of_days',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='trip',
            name='price',
            field=models.CharField(max_length=6),
        ),
    ]
