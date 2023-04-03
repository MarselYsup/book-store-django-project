# Book Store

Учебный проект по ПРСЧП КФУ

## Запуск проекта для разработки 

- `python3 -m venv venv` - создание виртуального окружения
- `source venv/bin/activate` - войти в виртуальное окружение Mac/Linux
- `venv\Scripts\activate` - войти в виртуальное окружение Windows
- `docker-compose up -d` - поднять postgres
- `pip install -r requirements.txt` - установка зависимостей
-  `python manage.py migrate` - применить миграции
-  `python manage.py createsuperuser` - создать суперпользователя
- `python manage.py runserver`  - запустить сервер для разработки на http://127.0.0.1:8000