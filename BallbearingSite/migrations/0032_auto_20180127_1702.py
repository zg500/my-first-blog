# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BallbearingSite', '0031_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=264, verbose_name='پست الکترونیکی'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(max_length=70, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=70, verbose_name='موضوع'),
        ),
    ]
