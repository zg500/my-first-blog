# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0042_sellerdesktop_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(verbose_name='آدرس', null=True, blank=True, max_length=264, validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ ._,/-]*$')]),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='companyname',
            field=models.CharField(verbose_name='نام شرکت', null=True, blank=True, max_length=128, validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ ._,/-]*$')]),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='tel',
            field=models.CharField(verbose_name='تلفن ثابت', null=True, blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='تلفن میبایست 11 رقم داشته باشد', regex='^\\d{11,11}$')]),
        ),
    ]
