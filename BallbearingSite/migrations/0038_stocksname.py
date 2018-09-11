# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0037_sellerdesktop'),
    ]

    operations = [
        migrations.CreateModel(
            name='StocksName',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128, verbose_name='نوع کالا')),
            ],
        ),
    ]
