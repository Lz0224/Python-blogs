# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='avatar/avatar.png', null=True, upload_to='avatar/%Y/%m'),
        ),
    ]
