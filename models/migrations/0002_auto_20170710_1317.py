# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]