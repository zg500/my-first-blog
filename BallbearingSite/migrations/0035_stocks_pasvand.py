# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0034_remove_stocks_suffix'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='pasvand',
            field=models.CharField(verbose_name='pasvand', blank=True, null=True, max_length=12),
        ),
    ]
