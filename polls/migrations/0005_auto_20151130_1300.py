# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_beat_beat_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='bass_kicks',
            field=models.CharField(default=b'empty', max_length=200),
        ),
        migrations.AddField(
            model_name='beat',
            name='snare_hits',
            field=models.CharField(default=b'empty', max_length=200),
        ),
    ]
