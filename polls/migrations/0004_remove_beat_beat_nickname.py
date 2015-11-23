# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_beat_beat_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beat',
            name='beat_nickname',
        ),
    ]
