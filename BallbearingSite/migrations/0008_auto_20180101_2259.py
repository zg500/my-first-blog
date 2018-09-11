# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0007_auto_20180101_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='confirmation',
            field=models.NullBooleanField(verbose_name='تایید'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='price',
            field=models.PositiveIntegerField(null=True, blank=True, verbose_name='قیمت'),
        ),
    ]
