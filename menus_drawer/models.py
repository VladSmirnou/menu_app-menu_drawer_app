import re

from django.core.validators import RegexValidator
from django.db import models


class Menu(models.Model):
    menu_name = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\w+$',
                message='Only [a-zA-Z0-9_] characters are allowed',
                flags=re.ASCII
            )
        ]
    )

    def __str__(self):
        return self.menu_name


class MenuNest(models.Model):
    menu_nest = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu_nest
