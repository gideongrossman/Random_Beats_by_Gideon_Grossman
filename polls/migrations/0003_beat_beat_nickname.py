# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_beat'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='beat_nickname',
            field=models.CharField(default='no nickname has been chosen', max_length=200),
            preserve_default=False,
        ),
    ]
