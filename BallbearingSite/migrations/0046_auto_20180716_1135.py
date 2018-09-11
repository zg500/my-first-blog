# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0045_auto_20180613_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'verbose_name': 'car', 'verbose_name_plural': 'cars'},
        ),
        migrations.AlterModelOptions(
            name='expiredays',
            options={'verbose_name': 'ExpireDay', 'verbose_name_plural': 'ExpireDays'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='stocks',
            options={'verbose_name': 'Stock', 'verbose_name_plural': 'Stocks'},
        ),
        migrations.AlterModelOptions(
            name='stocksname',
            options={'verbose_name': 'StocksName', 'verbose_name_plural': 'یییی'},
        ),
        migrations.AlterModelOptions(
            name='userprofileinfo',
            options={'verbose_name': 'UserProfileInfo', 'verbose_name_plural': 'UserProfileInfos'},
        ),
        migrations.AddField(
            model_name='parts',
            name='car',
            field=models.ForeignKey(null=True, to='BallbearingSite.Cars'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='cellphone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Phone number must be 11 digit.', regex='^\\d{11,11}$')], verbose_name='cellphone', null=True, max_length=17, blank=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='createDateTime',
            field=models.DateTimeField(auto_now=True, verbose_name='update date'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(verbose_name='email', max_length=264),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(verbose_name='title', max_length=70),
        ),
        migrations.AlterField(
            model_name='expiredays',
            name='days',
            field=models.PositiveIntegerField(verbose_name='expiredays', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='parts',
            name='confirm',
            field=models.CharField(max_length=12, verbose_name='confirmation', choices=[('pending', 'pending'), ('reject', 'reject'), ('approved', 'approved'), ('expired', 'expired')], default='pending'),
        ),
        migrations.AlterField(
            model_name='parts',
            name='date',
            field=models.DateTimeField(verbose_name='date', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='parts',
            name='pic',
            field=models.ImageField(verbose_name='pic', null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='parts',
            name='price',
            field=models.PositiveIntegerField(verbose_name='price', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='createDateTime',
            field=models.DateTimeField(auto_now=True, verbose_name='update date'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='owner',
            field=models.CharField(verbose_name='Owner', null=True, max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(verbose_name='title', max_length=70),
        ),
        migrations.AlterField(
            model_name='posts',
            name='updateDateTime',
            field=models.DateTimeField(verbose_name='create date', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sellerdesktop',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date', null=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='brand',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='brand must be in Capital letter', regex='^[A-Z]*$')], verbose_name='brand', max_length=64),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='comment',
            field=models.CharField(verbose_name='comment', null=True, max_length=264, blank=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='confirm',
            field=models.CharField(max_length=12, verbose_name='confirmation', choices=[('pending', 'pending'), ('reject', 'reject'), ('approved', 'approved'), ('expired', 'expired')], default='pending'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='date',
            field=models.DateTimeField(verbose_name='date', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='name',
            field=models.CharField(verbose_name='stockname', max_length=128),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='number',
            field=models.CharField(verbose_name='number', null=True, max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='pasvand',
            field=models.CharField(verbose_name='pasvand', null=True, max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='price',
            field=models.PositiveIntegerField(verbose_name='price', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stocksname',
            name='name',
            field=models.CharField(verbose_name='stockname', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Enter in Farsi letters', regex='^[0-9 آ-ی ء چ ._,/-]*$')], verbose_name='address', null=True, max_length=264, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='cellphone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Phone number must be 11 digit.', regex='^\\d{11,11}$')], verbose_name='cellphone', max_length=17),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='city',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Enter in Farsi letters', regex='^[0-9 آ-ی ء چ ._,/-]*$')], verbose_name='city', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='companyname',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Enter in Farsi letters', regex='^[0-9 آ-ی ء چ ._,/-]*$')], verbose_name='companyname', null=True, max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='state',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Enter in Farsi letters', regex='^[0-9 آ-ی ء چ ._,/-]*$')], verbose_name='state', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='tel',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Phone number must be 11 digit.', regex='^\\d{11,11}$')], verbose_name='tel', null=True, max_length=17, blank=True),
        ),
    ]
