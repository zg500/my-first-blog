# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0011_auto_20180111_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='confirm',
            field=models.CharField(null=True, verbose_name='تایید', choices=[('pending', 'pending'), ('reject', 'reject'), ('approved', 'approved'), ('expired', 'expired')], max_length=10),
        ),
    ]
