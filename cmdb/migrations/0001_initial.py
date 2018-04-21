# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-21 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('describe', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, unique=True)),
                ('ip', models.GenericIPAddressField(protocol='ipv4', unique=True)),
                ('cabinet', models.IntegerField(null=True)),
                ('cpu_model', models.CharField(max_length=128, null=True)),
                ('cpu_core', models.IntegerField(null=True)),
                ('mem', models.IntegerField(null=True)),
                ('disk', models.IntegerField(null=True)),
                ('OS', models.CharField(max_length=128, null=True)),
                ('product_model', models.CharField(max_length=128, null=True)),
                ('minions_status', models.CharField(default='undefined', max_length=32, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('detail', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Room'),
        ),
    ]
