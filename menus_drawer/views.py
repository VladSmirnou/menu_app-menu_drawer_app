from django.shortcuts import render


def home_page(request, menu_name, nest_lvl):
    return render(request, 'home.html')