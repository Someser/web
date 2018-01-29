# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_ques',
            new_name='book_ques_id',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_trip',
            new_name='book_trip_id',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_user',
            new_name='book_user_id',
        ),
    ]
