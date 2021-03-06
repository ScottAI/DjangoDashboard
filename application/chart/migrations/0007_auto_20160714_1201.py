# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0006_auto_20160713_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersPerChannelAndBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Other', models.IntegerField()),
                ('Direct', models.IntegerField()),
                ('Email', models.IntegerField()),
                ('Organic_Search', models.IntegerField()),
                ('Paid_Search', models.IntegerField()),
                ('Referral', models.IntegerField()),
                ('Social', models.IntegerField()),
                ('brand', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='UsersPerChannel',
        ),
        migrations.AlterUniqueTogether(
            name='usersperchannelandbrand',
            unique_together=set([('date', 'brand')]),
        ),
    ]
