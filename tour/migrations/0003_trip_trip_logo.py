# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_auto_20180128_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_logo',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
