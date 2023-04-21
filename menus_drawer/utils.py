import re

from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Menu


class MenuDrawer:
    
    def str_to_templ(self, context, menu_name):
        menu = Menu.objects.filter(menu_name=menu_name).prefetch_related('menunest_set').first()
        if not menu:
            return mark_safe(f'<div>There is no menu with this name [ {menu_name} ]</div>')
        
        self.initial_load = f"""
            <ul>
            <li><a href="{reverse('draw_menu_home', args=[menu.menu_name, '1'])}">{menu.menu_name}</a></li>
            </ul>
            """
        
        if res:= re.fullmatch(rf'/(\w+)/{ menu.menu_name }/(\d)/', context['request'].path):
            self.initial_load = self.add_layers(menu, res.group(1), res.group(2))

        return mark_safe(self.initial_load)
    
    def add_layers(self, menu, app_url, nest_lvl):
        if not (menus_objects:= menu.menunest_set.all()[:int(nest_lvl)]):
            return mark_safe(self.initial_load)
        
        self.inner_lists = """
            <ul>
            <li>Dummy text1</li>
            <li>Dummy text2</li>
            <li><a href="/{app_url}/%(menu_name)s/%(nest_lvl)s/">%(indent_name)s</a></li>
            </ul>
            """.format(app_url=app_url)

        for idx, obj in enumerate(menus_objects, 1):
            self.place = self.initial_load.rpartition('</li>')
            self.initial_load = self.place[0] + self.place[1] + \
                (self.inner_lists % {
                    'indent_name': obj.menu_nest,
                    'nest_lvl': idx + 1,
                    'menu_name': menu.menu_name,
                    }
                ) + self.place[2]
        
        return self.initial_load


str_converter = MenuDrawer()