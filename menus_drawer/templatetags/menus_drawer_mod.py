from django import template

from ..models import MenuNest
from ..utils import str_converter


register = template.Library()

@register.inclusion_tag('menus_drawer_temps/draw_menu.html')
def draw_menu(menu_name=None):
    if not (nest_objects:= MenuNest.objects.filter(menu__menu_name=menu_name)):
        return {
            'menu': f'{menu_name} (This menu name probably doesn\'t exist or doesn\'t have any relations)'
        }
    
    return {'menu': str_converter.str_to_templ(nest_objects, menu_name)}
