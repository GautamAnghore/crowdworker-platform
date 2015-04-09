# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20150409_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requester',
            name='requester',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='worker',
        ),
        migrations.AddField(
            model_name='person',
            name='about',
            field=models.TextField(default=datetime.datetime(2015, 4, 9, 2, 3, 15, 400970, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='who',
            field=models.CharField(default='w', max_length=1, choices=[(b'w', b'Worker'), (b'r', b'Requester')]),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Requester',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
