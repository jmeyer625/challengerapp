# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challengerapp', '0003_auto_20141116_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day_sequence',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
