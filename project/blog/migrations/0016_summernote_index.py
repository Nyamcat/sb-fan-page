# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-20 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20180621_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='summernote',
            name='index',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
