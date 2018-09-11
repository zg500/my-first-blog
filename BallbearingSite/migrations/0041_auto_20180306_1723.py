# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0040_auto_20180306_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='user',
            field=models.ForeignKey(null=True, related_name='stockdetails', to=settings.AUTH_USER_MODEL),
        ),
    ]
