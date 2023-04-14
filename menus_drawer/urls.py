from django.urls import path
from .views import home_page


urlpatterns = [
    path('drawer/<menu_name>/<int:nest_lvl>/', home_page),
]