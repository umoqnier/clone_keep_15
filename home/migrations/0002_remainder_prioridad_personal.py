# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='remainder',
            name='prioridad_personal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Prioridad'),
        ),
    ]
