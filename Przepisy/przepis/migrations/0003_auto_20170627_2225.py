# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('przepis', '0002_auto_20170627_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_logo',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_title',
            field=models.CharField(max_length=250),
        ),
    ]
