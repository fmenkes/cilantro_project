# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cilantro', '0003_recipe_servings'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default='default', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(unique=True, max_length=400),
            preserve_default=True,
        ),
    ]
