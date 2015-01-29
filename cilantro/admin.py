from django.contrib import admin
from cilantro.models import Category, Recipe, RecipeIngredient, Ingredient

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Ingredient)