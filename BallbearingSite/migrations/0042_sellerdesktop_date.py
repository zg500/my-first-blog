# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0041_auto_20180306_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerdesktop',
            name='date',
            field=models.DateTimeField(null=True, auto_now_add=True, verbose_name='تاریخ'),
        ),
    ]
