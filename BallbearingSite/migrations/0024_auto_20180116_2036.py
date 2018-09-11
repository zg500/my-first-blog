# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0023_auto_20180116_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='brand',
            field=models.CharField(verbose_name='مارک', validators=[django.core.validators.RegexValidator(message='مارک کالا را با حروف بزرگ انگلیسی وارد نمایید', regex='^[A-Z]*$')], max_length=64),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='name',
            field=models.CharField(verbose_name='نوع کالا', max_length=128),
        ),
    ]
