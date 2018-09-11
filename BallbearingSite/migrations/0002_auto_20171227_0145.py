# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name_plural': 'اطلاعات کاربران', 'verbose_name': 'اطلاعات کاربر'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=264, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='city',
            field=models.CharField(max_length=128, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='companyname',
            field=models.CharField(max_length=128, verbose_name='نام شرکت'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(unique=True, max_length=264, verbose_name='پست الکترونیکی'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='firstname',
            field=models.CharField(max_length=128, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastname',
            field=models.CharField(max_length=128, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='state',
            field=models.CharField(max_length=128, verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.CharField(max_length=12, verbose_name='تلفن'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(unique=True, max_length=128, verbose_name='نام کاربری'),
        ),
    ]
