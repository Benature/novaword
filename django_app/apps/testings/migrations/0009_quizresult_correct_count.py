# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-11 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testings', '0008_auto_20170929_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizresult',
            name='correct_count',
            field=models.IntegerField(default=0, verbose_name='\u7b54\u5bf9\u9898\u6570'),
        ),
    ]
