# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-21 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minions', '0003_auto_20180421_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='describe',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='OS',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='cabinet',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='cpu_core',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='cpu_model',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='disk',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='mem',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='product_model',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='detail',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
