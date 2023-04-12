from django.core.management.base import BaseCommand

from ...models import Menu


class Command(BaseCommand):
    MENUS = ['Menu_1', 'Menu_2', 'Menu_3']
    
    def handle(self, *args, **options):
        menus_obj = [Menu(menu_name=menu_name) for menu_name in self.MENUS]
        Menu.objects.bulk_create(menus_obj)

        counter = 2
        for menu in menus_obj:
            while counter != 5:
                menu.menunest_set.create(menu_nest=f'Menu {menu.id} nest {counter}')
                counter += 1
            counter = 2
