# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('plural', models.CharField(max_length=128, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('instructions', models.TextField()),
                ('servings', models.IntegerField(default=2, blank=True)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(to='cilantro.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('amount', models.CharField(max_length=40, blank=True)),
                ('value', models.IntegerField(default=0, blank=True)),
                ('unit', models.CharField(default=b'', max_length=40, blank=True)),
                ('recipe', models.ForeignKey(to='cilantro.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
