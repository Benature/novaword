# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-23 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_auto_20170821_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wordinunit',
            options={'verbose_name': '\u5355\u5143\u5355\u8bcd', 'verbose_name_plural': '\u5355\u5143\u5355\u8bcd'},
        ),
        migrations.AlterField(
            model_name='wordinunit',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.WordUnit', verbose_name='\u5355\u5143'),
        ),
        migrations.AlterField(
            model_name='wordinunit',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.Word', verbose_name='\u5355\u8bcd'),
        ),
    ]
