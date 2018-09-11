# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BallbearingSite', '0002_auto_20171227_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(verbose_name='پست الکترونیکی', max_length=264, unique=True)),
                ('firstname', models.CharField(verbose_name='نام', max_length=128)),
                ('lastname', models.CharField(verbose_name='نام خانوادگی', max_length=128)),
                ('companyname', models.CharField(verbose_name='نام شرکت', max_length=128)),
                ('tel', models.CharField(verbose_name='تلفن', max_length=12)),
                ('state', models.CharField(verbose_name='استان', max_length=128)),
                ('city', models.CharField(verbose_name='شهر', max_length=128)),
                ('address', models.CharField(verbose_name='آدرس', max_length=264)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
