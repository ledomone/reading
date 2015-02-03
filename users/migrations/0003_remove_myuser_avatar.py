# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_myuser_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='avatar',
        ),
    ]
