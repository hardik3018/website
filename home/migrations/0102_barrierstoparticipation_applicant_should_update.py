# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-25 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0101_auto_20180923_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrierstoparticipation',
            name='applicant_should_update',
            field=models.BooleanField(default=False),
        ),
    ]
