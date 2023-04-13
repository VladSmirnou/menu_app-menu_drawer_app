from django.shortcuts import render
from django.views import View

from .models import Menu
from .utils import interface


class HomePageView(View):

    def get(self, request):
        menus = Menu.objects.all()
        return render(request, 'home.html', {'menus': menus})


class MenusList(View):

    def get(self, request, menu_name, nest_lvl):
        menu_objects = Menu.objects.raw(
            'SELECT menus_app_menu.id, menus_app_menu.menu_name, menu_nest \
                FROM menus_app_menu LEFT OUTER JOIN menus_app_menunest \
                    ON menus_app_menu.id = menus_app_menunest.menu_id'
            )
        
        self.menu_number = int(menu_name.rsplit('_')[1])

        self.context = {
            'menus': interface.align_interface(menu_objects),
        }

        for lvl in range(1, nest_lvl + 1):
            if lvl == 1:
                self.context[f'menu{self.menu_number}_nest{lvl}'] = self.menu_number
                continue

            self.context[f'menu{self.menu_number}_nest{lvl}'] = True

        return render(request, 'home.html', self.context)