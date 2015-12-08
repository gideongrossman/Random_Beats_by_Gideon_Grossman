# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_beat_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='beat_pdf',
            field=models.ImageField(default=b'pic_folder/None/no-img.pdf', upload_to=b'pic_folder/'),
        ),
    ]
