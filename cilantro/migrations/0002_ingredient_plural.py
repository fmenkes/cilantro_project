# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cilantro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='plural',
            field=models.CharField(default='default', max_length=128),
            preserve_default=False,
        ),
    ]
