# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0006_auto_20171120_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='new_friend',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='user_firend',
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='friendships',
            field=models.ManyToManyField(related_name='_user_friendships_+', to='login_reg.User'),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]