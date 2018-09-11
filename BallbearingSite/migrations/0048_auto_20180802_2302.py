# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0047_auto_20180725_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='pic',
            field=models.ImageField(default='stocks/nopic.jpg', verbose_name='pic', null=True, blank=True, upload_to='stocks'),
        ),
    ]
