# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20160622_1523'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='site',
            unique_together=set([('url', 'active_start_date')]),
        ),
    ]
