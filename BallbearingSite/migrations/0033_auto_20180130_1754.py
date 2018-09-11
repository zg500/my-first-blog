# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0032_auto_20180127_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='owner',
            field=models.CharField(verbose_name='ثبت کننده', max_length=64, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ ._,/-]*$')], verbose_name='آدرس', max_length=264),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='city',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ ._,/-]*$')], verbose_name='شهر', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='companyname',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ ._,/-]*$')], verbose_name='نام شرکت', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='state',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ ._,/-]*$')], verbose_name='استان', max_length=128),
        ),
    ]
