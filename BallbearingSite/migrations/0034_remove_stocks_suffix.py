# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0033_auto_20180130_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks',
            name='suffix',
        ),
    ]
