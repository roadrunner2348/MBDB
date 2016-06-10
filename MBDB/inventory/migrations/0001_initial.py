# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_tag', models.IntegerField()),
                ('serial_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Homeroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('model_number', models.CharField(max_length=30)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('student_id', models.IntegerField()),
                ('homeroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Homeroom')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Program')),
            ],
        ),
    ]