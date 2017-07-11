# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20170710_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]
