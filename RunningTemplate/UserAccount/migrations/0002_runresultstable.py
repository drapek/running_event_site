# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 16:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserAccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunResultsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_5km', models.FloatField(verbose_name=b'5km_time')),
                ('time_overall', models.FloatField(verbose_name=b'10km_time')),
                ('runner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
