# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0005_auto_20180101_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='brand',
            field=models.CharField(verbose_name='مارک', max_length=64),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='comment',
            field=models.CharField(verbose_name='توصیفات', max_length=264),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='confirmation',
            field=models.BooleanField(verbose_name='تایید'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='date',
            field=models.DateTimeField(verbose_name='تاریخ', auto_now=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='number',
            field=models.IntegerField(verbose_name='شماره'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='seller',
            field=models.BooleanField(verbose_name='فروشنده'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='suffix',
            field=models.CharField(verbose_name='پسوند', max_length=12),
        ),
    ]
