# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0026_auto_20180121_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='ثبت کننده'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='updateDateTime',
            field=models.DateTimeField(verbose_name='تاریخ ساخت', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='confirm',
            field=models.CharField(default='درحال بررسی', choices=[('درحال بررسی', 'درحال بررسی'), ('رد', 'رد'), ('تایید', 'تایید'), ('منقضی', 'منقضی')], verbose_name='تایید', max_length=12),
        ),
    ]
