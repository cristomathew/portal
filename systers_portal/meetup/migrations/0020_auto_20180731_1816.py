# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-31 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0019_auto_20180731_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='venue',
            field=models.TextField(blank=True, verbose_name='Venue'),
        ),
    ]