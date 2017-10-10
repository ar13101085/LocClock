# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appuser',
            fields=[
                ('userId', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('message', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.TextField(max_length=32)),
                ('name1StartTime', models.TimeField()),
                ('name1EndTime', models.TimeField()),
                ('name2', models.TextField(max_length=32)),
                ('name2StartTime', models.TimeField()),
                ('name2EndTime', models.TimeField()),
                ('name3', models.TextField(max_length=32)),
                ('name3StartTime', models.TimeField()),
                ('name3EndTime', models.TimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.Appuser')),
            ],
        ),
    ]
