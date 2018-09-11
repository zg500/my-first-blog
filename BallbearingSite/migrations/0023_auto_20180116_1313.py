# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0022_auto_20180116_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks',
            name='docfile',
        ),
        migrations.AlterField(
            model_name='stocks',
            name='brand',
            field=models.CharField(null=True, validators=[django.core.validators.RegexValidator(message='مارک کالا را با حروف بزرگ انگلیسی وارد نمایید', regex='^[A-Z]*$')], verbose_name='مارک', blank=True, max_length=64),
        ),
    ]
