# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qualification', models.CharField(max_length=200)),
                ('dob', models.DateTimeField(verbose_name=b'Date of birth')),
                ('worker', models.ForeignKey(to='user_auth.Person')),
            ],
        ),
    ]
