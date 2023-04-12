from django.shortcuts import render
from django.views import View

from .models import Menu


class HomePageView(View):

    def get(self, request):
        menus = Menu.objects.all()
        return render(request, 'home.html', {'menus': menus})


class MenusList(View):

    def get(self, request, menu_name, nest_lvl):
        # Не знаю, как сделать чтобы был только 1 запрос тут
        menus = Menu.objects.prefetch_related('menunest_set')
        
        self.menu_number = int(menu_name.rsplit('_')[1])

        self.context = {
            'menus': menus,
        }

        for lvl in range(1, nest_lvl + 1):
            if lvl == 1:
                self.context[f'menu{self.menu_number}_nest{lvl}'] = self.menu_number
                continue

            self.context[f'menu{self.menu_number}_nest{lvl}'] = True

        return render(request, 'home.html', self.context)