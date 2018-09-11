# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0046_auto_20180716_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='stocksname',
            options={'verbose_name': 'StocksName', 'verbose_name_plural': 'StocksNames'},
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='number',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='pasvand',
        ),
    ]
