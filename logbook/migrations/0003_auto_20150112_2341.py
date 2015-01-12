# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0002_book_who'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(null=True, max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(null=True, max_length=250),
            preserve_default=True,
        ),
    ]
