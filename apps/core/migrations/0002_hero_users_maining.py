# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='users_maining',
            field=models.ManyToManyField(default=None, related_name='main_heros', to='login_registration.User'),
        ),
    ]
