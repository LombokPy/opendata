# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 12:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=20)),
                ('nama', models.CharField(max_length=35, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('img', models.ImageField(upload_to='member/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
