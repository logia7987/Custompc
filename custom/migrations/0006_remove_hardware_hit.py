# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-16 00:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0005_auto_20180416_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hardware',
            name='hit',
        ),
    ]
