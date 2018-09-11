# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0009_auto_20180102_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='brand',
            field=models.CharField(verbose_name='مارک', max_length=64, validators=[django.core.validators.RegexValidator(message='مارک کالا را با حروف بزرگ انگلیسی وارد نمایید', regex='^[A-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='date',
            field=models.DateTimeField(verbose_name='تاریخ', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(verbose_name='آدرس', max_length=264, validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ]*$')]),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='cellphone',
            field=models.CharField(verbose_name='تلفن همراه', blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='تلفن میبایست 11 رقم داشته باشد', regex='^\\d{11,11}$')]),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='city',
            field=models.CharField(verbose_name='شهر', max_length=128, validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ]*$')]),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='companyname',
            field=models.CharField(verbose_name='نام شرکت', max_length=128, validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ]*$')]),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='state',
            field=models.CharField(verbose_name='استان', max_length=128, validators=[django.core.validators.RegexValidator(message='با حروف فارسی وارد نمایید', regex='^[0-9 آ-ی ء چ]*$')]),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='tel',
            field=models.CharField(verbose_name='تلفن ثابت', blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='تلفن میبایست 11 رقم داشته باشد', regex='^\\d{11,11}$')]),
        ),
    ]
