from django import template

from ..utils import str_converter


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    return str_converter.str_to_templ(context, menu_name)
