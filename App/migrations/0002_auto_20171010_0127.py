# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='name1',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='name1EndTime',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='name1StartTime',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='name2EndTime',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='name2StartTime',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='name3',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='name3EndTime',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='name3StartTime',
            field=models.CharField(max_length=32),
        ),
    ]
