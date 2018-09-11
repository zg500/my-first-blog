# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0003_auto_20171229_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='email',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(max_length=264, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='city',
            field=models.CharField(max_length=128, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='companyname',
            field=models.CharField(max_length=128, verbose_name='companyname'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='firstname',
            field=models.CharField(max_length=128, verbose_name='firstname'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='lastname',
            field=models.CharField(max_length=128, verbose_name='lastname'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='state',
            field=models.CharField(max_length=128, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='tel',
            field=models.CharField(max_length=12, verbose_name='tel'),
        ),
    ]
