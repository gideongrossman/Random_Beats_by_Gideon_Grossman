# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_beat_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beat',
            name='pub_date',
        ),
    ]
