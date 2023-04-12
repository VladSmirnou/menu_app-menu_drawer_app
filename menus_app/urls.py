from django.urls import path

from .views import HomePageView, MenusList


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('menus/<menu_name>/<int:nest_lvl>/', MenusList.as_view(), name='menus'),
]
