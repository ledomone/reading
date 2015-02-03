# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_myuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(upload_to='avatars/', blank=True, null=True),
            preserve_default=True,
        ),
    ]
