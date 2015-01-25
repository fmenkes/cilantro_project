from django.db import models
from django.template.defaultfilters import slugify

import re

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Recipe(models.Model):
    category = models.ForeignKey(Category)
    # TODO: the name of recipes should not be unique, but it should be unique to its category.
    name = models.CharField(max_length=400)
    instructions = models.TextField()
    servings = models.IntegerField(blank=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


"""class ArchetypeIngredient(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name"""


class Ingredient(models.Model):
    # TODO: many to many relationship? Is there a way to decouple the amount from the ingredient?
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=128)
    amount = models.CharField(max_length=40, blank=True)
    unit = models.CharField(max_length=40, blank=True, default="")

    def save(self, *args, **kwargs):
        """finds the unit in the amount and saves it to the (hidden) unit field."""
        # This regex needs lots of work!
        pattern = re.compile(r'\d+(\s|\W)*(\D*)$')
        unit = pattern.search(str(self.amount))
        if unit:
            self.unit = unit.groups()[1]
        else:
            self.unit = ''
        super(Ingredient, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
