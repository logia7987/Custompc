# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-13 06:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0003_remove_custom_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custom',
            options={'ordering': ['create_date']},
        ),
    ]
