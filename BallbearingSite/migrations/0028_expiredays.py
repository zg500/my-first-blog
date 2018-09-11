# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0027_auto_20180124_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpireDays',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('days', models.PositiveIntegerField(blank=True, verbose_name='expiredays', null=True)),
            ],
        ),
    ]
