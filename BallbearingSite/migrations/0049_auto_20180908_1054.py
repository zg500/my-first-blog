# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0048_auto_20180802_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks',
            name='user',
        ),
        migrations.DeleteModel(
            name='StocksName',
        ),
        migrations.AlterModelOptions(
            name='cars',
            options={'verbose_name_plural': 'cars', 'verbose_name': 'car', 'ordering': ('carname',)},
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='is_seller',
        ),
        migrations.AddField(
            model_name='cars',
            name='confirm',
            field=models.CharField(choices=[('pending', 'pending'), ('reject', 'reject'), ('approved', 'approved'), ('expired', 'expired')], max_length=12, verbose_name='confirmation', default='pending'),
        ),
        migrations.AlterField(
            model_name='sellerdesktop',
            name='stock',
            field=models.ForeignKey(to='BallbearingSite.Parts', blank=True, related_name='stocktoseller', null=True),
        ),
        migrations.DeleteModel(
            name='Stocks',
        ),
    ]
