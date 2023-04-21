from django.urls import path
from .views import home_page


urlpatterns = [
    path('<menu_name>/<int:nest_lvl>/', home_page, name='draw_menu_home'),
]