# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waliki', '0005_auto_20141124_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='status_code',
            field=models.IntegerField(choices=[(302, '302 Found'), (301, '301 Moved Permanently')], default=302),
        ),
    ]
