## Installation
```
Последовательность установки:
  1) Установить зависимости: 
  pip install -r requirements.txt (тут только debug toolbar и Django)
  
  2) Миграций нету, поэтому:
  py manage.py makemigrations menus_app; py manage.py makemigrations menus_drawer; py manage.py migrate

  3) Для моделей 'menus_app' присутствует seeder, поэтому можно запустить команду:
  py manage.py seed_app_db (Так приложение гарантированно будет функционировать)

  4) Переменные окружения не требуются, Debug выставлен в True

  5) Главный URL приложения -> http://127.0.0.1:8000/menus_app/
```

## Tips
1) Если добавлять обьекты в приложении 'menus_app' самостоятельно, то значения поля 'menu_name' модели 
'Menu' должны оканчиваться одинарным нижним подчеркиванием и номером 1, 2 и 3 (делал только на 3 меню)
например -> 'Menu_1'. ID обьекта 'Menu' в базе данных и номер после нижнего подчеркивания 
в поле 'menu_name' должны совпадать. Обьекты модели 'MenuNest' могут иметь любое имя.
2) Для приложения 'menus_drawer' надо иметь обьект таблицы 'Menu' (в двух приложениях имена моделей одиаковые)
в базе. Имя меню в тэге и в базе данных должны совпадать, а также иметь один или более связанных обьектов. В противном случае отобразится имя несуществующего (или существующего, но без связей) меню и подсказка. Каких либо ограничений по именам, id и т.д. для обьектов модели 'Menu' и связанных с ними обьектов модели 'MenuNest' нет.
3) Чтобы нарисовать меню, надо добавить на страницу -> {% load menus_drawer_mod %} и {% draw_menu 'menu_name' %}