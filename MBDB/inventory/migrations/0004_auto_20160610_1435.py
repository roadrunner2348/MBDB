# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_device_model'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Program',
            new_name='Group',
        ),
        migrations.RemoveField(
            model_name='student',
            name='program',
        ),
        migrations.AddField(
            model_name='device',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Group'),
        ),
        migrations.AddField(
            model_name='device',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Group'),
        ),
    ]