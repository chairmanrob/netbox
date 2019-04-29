# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-13 17:14
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0004_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantgroup',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tenantgroup',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]