# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170723_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='avatar/avatar.png', null=True, upload_to='avatar'),
        ),
    ]