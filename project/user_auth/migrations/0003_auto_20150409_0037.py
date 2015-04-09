# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_auto_20150409_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=datetime.datetime(2015, 4, 8, 19, 7, 7, 58703, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requester',
            name='requester',
            field=models.ForeignKey(to='user_auth.Person'),
        ),
    ]
