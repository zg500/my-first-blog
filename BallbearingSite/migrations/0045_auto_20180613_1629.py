# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BallbearingSite', '0044_auto_20180312_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('carname', models.CharField(verbose_name='carname', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('partname', models.CharField(verbose_name='partname', max_length=128)),
                ('pic', models.ImageField(upload_to='', null=True, blank=True)),
                ('description', models.CharField(null=True, max_length=264, verbose_name='description', blank=True)),
                ('price', models.PositiveIntegerField(null=True, verbose_name='قیمت', blank=True)),
                ('date', models.DateTimeField(verbose_name='تاریخ', auto_now_add=True)),
                ('confirm', models.CharField(choices=[('درحال بررسی', 'درحال بررسی'), ('رد', 'رد'), ('تایید', 'تایید'), ('منقضی', 'منقضی')], default='درحال بررسی', verbose_name='تایید', max_length=12)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Part',
                'verbose_name_plural': 'Parts',
            },
        ),
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(verbose_name='عنوان', max_length=70),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(verbose_name='عنوان', max_length=70),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='is_seller',
            field=models.CharField(verbose_name='sell', max_length=2),
        ),
    ]
