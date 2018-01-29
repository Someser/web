# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('statement', models.TextField(max_length=6000, null=True)),
                ('answer', models.TextField(default=b' ')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('destination', models.CharField(max_length=50)),
                ('transport', models.CharField(max_length=9)),
                ('is_available', models.BooleanField(default=True)),
                ('trip_id', models.AutoField(serialize=False, primary_key=True)),
                ('price', models.IntegerField()),
                ('no_of_days', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='ques_id',
            field=models.ForeignKey(related_name='questions', to='tour.Trip'),
        ),
        migrations.AddField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='book_ques',
            field=models.ForeignKey(to='tour.Question'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_trip',
            field=models.ForeignKey(to='tour.Trip'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
