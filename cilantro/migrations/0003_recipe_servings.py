# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cilantro', '0002_ingredient_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
