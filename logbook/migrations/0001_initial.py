# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('pages', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
