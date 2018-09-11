# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0043_auto_20180311_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='is_seller',
            field=models.CharField(verbose_name='فروشنده', max_length=2, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='pasvand',
            field=models.CharField(verbose_name='پسوند', max_length=12, blank=True, null=True),
        ),
    ]
