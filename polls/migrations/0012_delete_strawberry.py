# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_strawberry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Strawberry',
        ),
    ]
