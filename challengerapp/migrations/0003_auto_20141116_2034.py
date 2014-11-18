# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challengerapp', '0002_auto_20141116_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(null=True, verbose_name=b'date published')),
                ('day', models.ForeignKey(to='challengerapp.Day')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='completed_at',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='post',
            field=models.ForeignKey(default=None, to='challengerapp.Post'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='challenge',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='challenge',
            field=models.ForeignKey(default=None, to='challengerapp.Challenge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='day',
            field=models.ForeignKey(default=None, to='challengerapp.Day'),
            preserve_default=True,
        ),
    ]
