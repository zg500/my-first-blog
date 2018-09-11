# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0038_stocksname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerdesktop',
            name='buyer',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, related_name='buyer', null=True),
        ),
        migrations.AlterField(
            model_name='sellerdesktop',
            name='seller',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, related_name='seller', null=True),
        ),
        migrations.AlterField(
            model_name='sellerdesktop',
            name='stock',
            field=models.ForeignKey(blank=True, related_name='stocktoseller', to='BallbearingSite.Stocks', null=True),
        ),
    ]
