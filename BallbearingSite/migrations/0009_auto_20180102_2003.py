# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BallbearingSite', '0008_auto_20180101_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stocks',
            options={'verbose_name': 'کالا', 'verbose_name_plural': 'کالاها'},
        ),
        migrations.AlterModelOptions(
            name='userprofileinfo',
            options={'verbose_name': 'UserProfileInfo', 'verbose_name_plural': 'UserProfileInfos'},
        ),
        migrations.AddField(
            model_name='stocks',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='name',
            field=models.CharField(verbose_name='نوع کالا', max_length=128),
        ),
    ]
