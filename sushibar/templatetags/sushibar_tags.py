from django import template
from sushibar.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('sushibar/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {"cats": cats}
