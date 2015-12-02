# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_beat_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beat',
            name='photo',
        ),
    ]
