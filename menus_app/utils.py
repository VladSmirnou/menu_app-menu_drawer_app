from collections import defaultdict


class InterfaceHelper:

    def align_interface(self, menu_objects):
        '''
        Нужна, чтобы HomePageView и MenusList отдавали
        информацию на главную страницу в схожем формате
        '''
        sep_menus = defaultdict(list)
        for menu in menu_objects:
            sep_menus[menu].append(menu.menu_nest)
            menu.nest = sep_menus[menu] 
        
        return sep_menus
    

interface = InterfaceHelper()

