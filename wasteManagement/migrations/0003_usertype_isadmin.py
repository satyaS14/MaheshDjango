# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-17 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasteManagement', '0002_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertype',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]
