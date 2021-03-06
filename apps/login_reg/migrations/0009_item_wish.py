# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-22 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0008_auto_20171121_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='login_reg.User')),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('wish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishers', to='login_reg.Item')),
                ('wisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='login_reg.User')),
            ],
        ),
    ]
