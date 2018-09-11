# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0021_auto_20180116_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='نوع کالا'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='number',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='شماره'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='suffix',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='پسوند'),
        ),
    ]
