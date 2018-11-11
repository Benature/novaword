# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-11 14:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learn', '0017_auto_20181108_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordbook',
            name='maintainers',
            field=models.ManyToManyField(related_name='maintainer', to=settings.AUTH_USER_MODEL),
        ),
    ]
