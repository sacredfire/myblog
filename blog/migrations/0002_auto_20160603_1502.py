# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authour',
            new_name='author',
        ),
    ]
