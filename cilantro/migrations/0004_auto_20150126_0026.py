# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cilantro', '0003_auto_20150125_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='ingredient_type',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=2, blank=True),
            preserve_default=True,
        ),
    ]
