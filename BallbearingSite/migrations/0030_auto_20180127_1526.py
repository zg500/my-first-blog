# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0029_auto_20180126_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expiredays',
            options={'verbose_name_plural': 'زمان انقضا', 'verbose_name': 'زمان انقضا'},
        ),
    ]
