from django import template
from cilantro.models import Category

register = template.Library()


@register.inclusion_tag('cilantro/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(), 'act_cat': cat}