# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0012_stocks_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='confirm',
            field=models.CharField(choices=[('درحال بررسی', 'درحال بررسی'), ('رد', 'رد'), ('تایید', 'تایید'), ('منقضی', 'منقضی')], default='درحال بررسی', verbose_name='تایید', max_length=10),
        ),
    ]
