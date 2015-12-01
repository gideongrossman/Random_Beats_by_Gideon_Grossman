# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_remove_beat_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beat',
            options={'get_latest_by': 'creation_date'},
        ),
        migrations.AddField(
            model_name='beat',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
