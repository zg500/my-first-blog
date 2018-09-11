# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BallbearingSite', '0036_remove_stocks_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerDesktop',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('buyer', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='buyer')),
                ('seller', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='seller')),
                ('stock', models.ForeignKey(to='BallbearingSite.Stocks')),
            ],
            options={
                'verbose_name': 'SellerDesktop',
                'verbose_name_plural': 'SellerDesktop',
            },
        ),
    ]
