# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-18 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='mp3_uk_url',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u82f1\u5f0f\u53d1\u97f3mp3'),
        ),
        migrations.AddField(
            model_name='word',
            name='mp3_us_url',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u7f8e\u5f0f\u53d1\u97f3mp3'),
        ),
    ]
