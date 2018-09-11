# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0013_auto_20180111_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks',
            name='confirmation',
        ),
        migrations.AlterField(
            model_name='stocks',
            name='comment',
            field=models.CharField(blank=True, max_length=264, verbose_name='توصیفات', null=True),
        ),
    ]
