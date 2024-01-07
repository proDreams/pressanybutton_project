# Проект "Код на салфетке"

## Описание:

Репозиторий проекта "Код на салфетке". Включает в себя актуальные файлы к постам "[Сайт на Django](https://pressanybutton.ru/category/sajt-na-django/?utm_source=github&utm_medium=repo&utm_campaign=readme)" и "[Telegram-бот на AIOgram3](https://pressanybutton.ru/category/telegram-bot-na-aiogram3/?utm_source=github&utm_medium=repo&utm_campaign=readme)".

## Статьи по разработке данного проекта доступны на сайте [pressanybutton.ru](https://pressanybutton.ru?utm_source=github&utm_medium=repo&utm_campaign=readme)

<details>
<summary>
  <strong>
    Статьи по проекту:
  </strong>
</summary>

1. [Django 1. Установка Django](https://pressanybutton.ru/post/sajt-na-django/django-1-ustanovka-django/?utm_source=github&utm_medium=repo&utm_campaign=readme)
2. [Django 2. Создание проекта](https://pressanybutton.ru/post/sajt-na-django/django-2-sozdanie-proekta/?utm_source=github&utm_medium=repo&utm_campaign=readme)
3. [Django 3. Базовая конфигурация](https://pressanybutton.ru/post/sajt-na-django/django-3-bazovaya-konfiguraciya/?utm_source=github&utm_medium=repo&utm_campaign=readme) - 
4. [Django 4. Суперпользователь и первый запуск](https://pressanybutton.ru/post/sajt-na-django/django-4-superpolzovatel-i-pervyj-zapusk/?utm_source=github&utm_medium=repo&utm_campaign=readme)
5. 

</details>

## Запуск
_Инструкция будет изменяться/дополняться по мере развития проекта_

### Запуск Django
1. Клонировать репозиторий:
    ```powershell
    git clone https://github.com/proDreams/pressanybutton_project.git
    ```
2. Установить зависимости:
    ```powershell
    pip install -r requirements.txt
    ```
3. Применить миграции для создания БД:
    ```powershell
    python manage.py migrate
    ```
4. Создать суперпользователя:
    ```powershell
    python manage.py createsuperuser
    ```
5. Запустить веб-сервер:
    ```powershell
    python manage.py runserver
    ```

## Автор:

Иван Ашихмин