# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=264)),
                ('companyname', models.CharField(max_length=128)),
                ('tel', models.CharField(max_length=12)),
                ('email', models.EmailField(unique=True, max_length=264)),
                ('state', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('username', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
