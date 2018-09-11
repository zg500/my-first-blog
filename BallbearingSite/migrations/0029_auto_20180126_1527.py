# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0028_expiredays'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expiredays',
            options={'verbose_name_plural': 'ExpireDays', 'verbose_name': 'ExpireDay'},
        ),
        migrations.AlterField(
            model_name='expiredays',
            name='days',
            field=models.PositiveIntegerField(null=True, verbose_name='زمان انقضا', blank=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='seller',
            field=models.BooleanField(verbose_name='فروشنده'),
        ),
    ]
