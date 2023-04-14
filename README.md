## Installation
```
Последовательность установки:
  1) Установить зависимости: 
  pip install -r requirements.txt (тут только debug toolbar и Django)
  
  2) Миграций нету, поэтому:
  py manage.py makemigrations menus_app; py manage.py makemigrations menus_drawer; py manage.py migrate

  3) Для моделей 'menus_app' присутствует seeder, поэтому можно запустить команду:
  py manage.py seed_app_db (Так приложение 'menus_app' гарантированно будет функционировать)

  4) Создать пользователя:
  py manage.py createsuperuser --username Admin --email Admin@gmail.com

  5) Переменные окружения не требуются, Debug выставлен в True

  6) Главный URL приложения -> http://127.0.0.1:8000/menus_app/
```

## Tips
1) Если добавлять объекты в приложении 'menus_app' самостоятельно, то значения поля 'menu_name' модели 
'Menu' должны оканчиваться одинарным нижним подчеркиванием и номером 1, 2 и 3 (делал только на 3 меню)
например -> 'Menu_1'. ID объекта 'Menu' в базе данных и номер после нижнего подчеркивания 
в поле 'menu_name' должны совпадать. Объекты модели 'MenuNest' могут иметь любое имя.
2) Для приложения 'menus_drawer' нужно создать объект (или объекты) таблицы 'Menu' (в двух приложениях имена
моделей одинаковые) в панели Администратора. После этого можно создавать объекты таблицы 'MenuNest'.
Имя оъекта таблицы 'Menu' должно совпадать с именем, указанным в {% draw_menu 'menu name' %}. Для создания имени
объектов таблицы 'Menu' доспуны только [a-zA-Z0-9_] (flag=re.ASCII) символы. В остальном ораничений нет.
3) Чтобы нарисовать меню, надо добавить на страницу -> {% load menus_drawer_mod %} и {% draw_menu 'menu_name' %}.
