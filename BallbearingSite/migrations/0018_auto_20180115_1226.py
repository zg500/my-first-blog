# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0017_auto_20180115_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='seller',
            field=models.BooleanField(default='null', verbose_name='فروشنده'),
        ),
    ]
