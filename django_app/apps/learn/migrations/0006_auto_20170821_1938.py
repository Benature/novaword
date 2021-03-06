# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-21 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_wordunit_words'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordInUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1, verbose_name='顺序')),
            ],
            options={
                'verbose_name': 'Words in unit',
                'verbose_name_plural': 'Words in unit',
            },
        ),
        migrations.RemoveField(
            model_name='wordunit',
            name='words',
        ),
        migrations.AddField(
            model_name='wordinunit',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.WordUnit', verbose_name='Unit'),
        ),
        migrations.AddField(
            model_name='wordinunit',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.Word', verbose_name='Word'),
        ),
    ]
