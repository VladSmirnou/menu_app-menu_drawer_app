from django.contrib import admin

from .models import Menu, MenuNest


admin.site.register([Menu, MenuNest])