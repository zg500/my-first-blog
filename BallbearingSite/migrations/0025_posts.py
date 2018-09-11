# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BallbearingSite', '0024_auto_20180116_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField()),
                ('updateDateTime', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('createDateTime', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='asd')),
            ],
        ),
    ]
