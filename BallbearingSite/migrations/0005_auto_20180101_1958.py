# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0004_auto_20171229_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='نام')),
                ('number', models.IntegerField(verbose_name='number')),
                ('suffix', models.CharField(max_length=12, verbose_name='uffix')),
                ('brand', models.CharField(max_length=64, verbose_name='brand')),
                ('comment', models.CharField(max_length=264, verbose_name='comment')),
                ('price', models.IntegerField(verbose_name='price')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('confirmation', models.BooleanField(verbose_name='confirmation')),
                ('seller', models.BooleanField(verbose_name='seller')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='lastname',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cellphone',
            field=models.CharField(verbose_name='تلفن همراه', validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], blank=True, max_length=17),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(max_length=264, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='city',
            field=models.CharField(max_length=128, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='companyname',
            field=models.CharField(max_length=128, verbose_name='نام شرکت'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='state',
            field=models.CharField(max_length=128, verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='tel',
            field=models.CharField(verbose_name='تلفن ثابت', validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], blank=True, max_length=17),
        ),
    ]
