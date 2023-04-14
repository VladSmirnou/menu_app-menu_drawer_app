import re

from django.utils.safestring import mark_safe

from .models import Menu


class MenuDrawer:

    def str_to_templ(self, context, menu_name):
        menus = Menu.objects.prefetch_related('menunest_set')
        
        try:
            menu = menus.get(menu_name=menu_name)
        except:
            return mark_safe(f'<div>There is no menu with this name [ {menu_name} ]</div>')

        self.initial_load = f"""
            <ul>
            <li><a href="/menus_drawer/drawer/{menu.menu_name}/1/">{menu.menu_name}</a></li>
            </ul>
            """

        if re.match(r'(?=.*/%s/)' % menu.menu_name, context['request'].path):
            self.initial_load = self.add_layers(menu, context)
            
        return mark_safe(self.initial_load)
    
    def add_layers(self, menu, context):
        self.nest_lvl = int(context['request'].path[-2])
        if not (menus_objects:= menu.menunest_set.all()[:self.nest_lvl]):
            return mark_safe(self.initial_load)

        self.inner_lists = """
            <ul>
            <li>Dummy text1</li>
            <li>Dummy text2</li>
            <li><a href="/menus_drawer/drawer/%(menu_name)s/%(nest_lvl)s/">%(indent_name)s</a></li>
            </ul>"""

        for idx, obj in enumerate(menus_objects, 1):
            place = self.initial_load.rpartition('</li>')
            self.initial_load = place[0] + place[1] + \
                (self.inner_lists % {
                    'indent_name': obj.menu_nest,
                    'nest_lvl': idx + 1,
                    'menu_name': menu.menu_name,
                    }
                ) + place[2]
        
        return self.initial_load


str_converter = MenuDrawer()