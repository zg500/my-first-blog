# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0039_auto_20180306_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerdesktop',
            name='buyer',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='buyer'),
        ),
        migrations.AlterField(
            model_name='sellerdesktop',
            name='seller',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='seller'),
        ),
    ]
