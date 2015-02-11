from django import template
from cilantro.models import Category, Recipe, RecipeIngredient

register = template.Library()

@register.inclusion_tag('cilantro/cats.html')
def get_category_list(user, cat=None):
    return {'cats': Category.objects.filter(user=user), 'act_cat': cat, 'recipes': Recipe.objects.all(), 'user': user}

"""
@register.inclusion_tag('cilantro/list.html')
def make_shopping_list(recipe):
    return {'recipe': recipe, 'ingredients': RecipeIngredient.objects.filter(recipe=recipe)}"""