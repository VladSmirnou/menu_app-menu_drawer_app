from django.template import Context, Template


class MenuDrawer:

    def str_to_templ(self, nest_objects, menu_name):
        self.default_string = """
        <ul>
        <li><a href="#">{{ menu_name }}</a></li>
        </ul>
        """
        self.indent = """
        <ul>
        <li>Dummy text1</li>
        <li>Dummy text2</li>
        <li><a href="#">%(indent_name)s</a></li>
        </ul>"""
        
        for i in range(1, nest_objects.count() + 1):
            self.place = self.default_string.rpartition('</li>')
            self.default_string = self.place[0] + self.place[1] + \
                (self.indent % {'indent_name': nest_objects[i - 1].menu_nest}) + self.place[2]

        template = Template(self.default_string)
        context = Context({'menu_name': menu_name})
        return template.render(context)


str_converter = MenuDrawer()