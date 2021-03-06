# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20170710_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='NestedComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nested_comment_text', models.CharField(max_length=1000, verbose_name=b'nested_comment_text')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Comment')),
            ],
        ),
    ]
