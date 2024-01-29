# Тестовое задание Mirgovorit

### Используемый стек 
  - Python 3.10
  - Django 5.0.1
  - Postgresql

### Дата релиза 29.01.2024

## Настройка и запуск проекта

### Подключение PostgreSQL

1. Скачать и установить PostgreSQL локально
2. Создать базу данных для проекта командой:

```sql
CREATE
DATABASE cookbook;
```

3. Создать пользователя и дать ему необходимые права командами:

```sql
CREATE
USER "Ваше имя пользователя" WITH PASSWORD "Ваш пароль";
ALTER
USER "Ваше имя пользователя" WITH SUPERUSER;
```

4. Выполняем миграции в django командой:

```bash
python manage.py migrate
```

### Настройка переменных окружения

Скопировать содержимое файла `env.template` в файл `.env` и указать необходимые значения переменных окружения, например:

```bash
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

### Установка зависимостей в виртуальное окружение

```bash
pip install -r requirements.txt
```

