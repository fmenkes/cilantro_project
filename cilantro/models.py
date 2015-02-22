from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import re


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    user = models.ForeignKey(User)
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
    user = models.ForeignKey(User)
    # TODO: the name of recipes should not be unique, but it should be unique to its category.
    name = models.CharField(max_length=400, unique=True)
    instructions = models.TextField(blank=True)
    servings = models.IntegerField(blank=True, default=2)
    is_shopping_list = models.BooleanField(default=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient 'archetype'."""
    name = models.CharField(max_length=128, unique=True)
    plural = models.CharField(max_length=128, blank=True)

    """def save(self, *args, **kwargs):

        super(Ingredient, self).save(*args, **kwargs)"""

    def __unicode__(self):
        return self.name


class RecipeIngredient(models.Model):
    """Each RecipeIngredient is 1. a certain ingredient e.g. 'Tomato' and 2. an amount e.g. '400g'."""
    name = models.CharField(max_length=128)
    recipe = models.ForeignKey(Recipe)
    amount = models.CharField(max_length=40, blank=True)
    value = models.IntegerField(blank=True, default=0)
    unit = models.CharField(max_length=40, blank=True, default="")

    def save(self, *args, **kwargs):
        """finds the unit in the amount and saves it to the (hidden) unit and value fields."""
        # This regex needs lots of work!
        pattern = re.compile(r'(\d+)(\s|\W)*(\D*)$')
        result = pattern.search(str(self.amount))
        if result:
            self.unit = result.groups()[2]
            self.value = result.groups()[0]
        super(RecipeIngredient, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
