# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-15 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180105_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='aliconfig',
            name='JDName',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='JD广告位名称'),
        ),
        migrations.AddField(
            model_name='aliconfig',
            name='JDPid',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='JDId', to='myapp.Agent', verbose_name='JD广告位'),
        ),
    ]