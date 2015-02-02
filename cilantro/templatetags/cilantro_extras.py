from django import template
from cilantro.models import Category, Recipe

register = template.Library()

@register.inclusion_tag('cilantro/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(), 'act_cat': cat, 'recipes': Recipe.objects.all()}