# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170724_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='./upload/'),
        ),
    ]
