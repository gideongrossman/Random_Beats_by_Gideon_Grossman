# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20151130_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='photo',
            field=models.ImageField(default='dude.jpg', upload_to=b'cars'),
            preserve_default=False,
        ),
    ]
