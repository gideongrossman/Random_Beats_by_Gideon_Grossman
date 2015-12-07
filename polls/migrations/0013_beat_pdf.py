# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_delete_strawberry'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='pdf',
            field=models.FileField(null=True, upload_to=b'sheet_music/%Y/%m'),
        ),
    ]
