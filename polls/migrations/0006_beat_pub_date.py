# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20151130_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 23, 17, 33, 628000, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
