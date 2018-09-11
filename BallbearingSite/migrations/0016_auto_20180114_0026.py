# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0015_stocks_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='seller',
            field=models.BooleanField(verbose_name='فروشنده', default=1),
        ),
    ]
