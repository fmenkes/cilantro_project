# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cilantro', '0002_ingredient_plural'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='plural',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
