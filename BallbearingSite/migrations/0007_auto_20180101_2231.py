# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0006_auto_20180101_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='number',
            field=models.CharField(max_length=64, verbose_name='شماره'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='price',
            field=models.PositiveIntegerField(verbose_name='قیمت'),
        ),
    ]
