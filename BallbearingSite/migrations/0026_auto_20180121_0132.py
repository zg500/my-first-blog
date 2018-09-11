# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0025_posts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'پستها', 'verbose_name': 'پست'},
        ),
        migrations.AlterModelOptions(
            name='userprofileinfo',
            options={'verbose_name_plural': 'اطلاعات کاربران', 'verbose_name': 'اطلاعات کاربر'},
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='createDateTime',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='cellphone',
            field=models.CharField(verbose_name='تلفن همراه', validators=[django.core.validators.RegexValidator(message='تلفن میبایست 11 رقم داشته باشد', regex='^\\d{11,11}$')], max_length=17),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='tel',
            field=models.CharField(verbose_name='تلفن ثابت', validators=[django.core.validators.RegexValidator(message='تلفن میبایست 11 رقم داشته باشد', regex='^\\d{11,11}$')], max_length=17),
        ),
    ]
