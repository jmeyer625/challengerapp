# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__


class Migration(migrations.Migration):

    dependencies = [
        ('challengerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day_sequence',
            field=models.IntegerField(verbose_name=__builtin__.max),
            preserve_default=True,
        ),
    ]
