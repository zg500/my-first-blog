# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0030_auto_20180127_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=70)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوا')),
                ('cellphone', models.CharField(max_length=17, null=True, verbose_name='تلفن همراه', validators=[django.core.validators.RegexValidator(message='تلفن میبایست 11 رقم داشته باشد', regex='^\\d{11,11}$')], blank=True)),
                ('email', models.EmailField(max_length=264, unique=True, verbose_name='پست الکترونیکی')),
                ('createDateTime', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
            ],
            options={
                'verbose_name_plural': 'پیغام\u200cها',
                'verbose_name': 'Message',
            },
        ),
    ]
