# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170729_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogtype',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]