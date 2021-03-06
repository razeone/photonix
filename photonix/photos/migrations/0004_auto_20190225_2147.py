# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-25 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20190225_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete_with_children',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='photos.Task'),
        ),
    ]
