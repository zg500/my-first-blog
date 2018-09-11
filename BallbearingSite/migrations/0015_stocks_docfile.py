# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0014_auto_20180113_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='docfile',
            field=models.FileField(blank=True, upload_to='documents/', null=True),
        ),
    ]
