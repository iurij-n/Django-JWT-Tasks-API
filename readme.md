# Django JWT Auth & Tasks API

Простое API на Django с аутентификацией через JWT и возможностью управления задачами.

## 🔧 Стек технологий
- Python 3.8
- Django REST Framework
- djangorestframework-simplejwt
- django-cors-headers
- SQLite (по умолчанию, можно заменить)

## 🚀 Возможности
- Регистрация и вход пользователя через JWT
- Обновление и выход из системы
- Полный CRUD для задач (создание, просмотр, обновление, удаление)
- Фильтрация задач по статусу выполнения
- Авторизация через JWT-токен
- Сортировка задач по переданному ключу

## 📦 Установка и запуск

### 1️⃣ Клонирование репозитория
```sh
git clone https://github.com/iurij-n/Django-JWT-Tasks-API.git
```

### 2️⃣ Создание и активация виртуального окружения
```sh
python -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate  # для Windows
```

### 3️⃣ Установка зависимостей
```sh
pip install -r requirements.txt
```

### 4️⃣ Применение миграций и создание суперпользователя
```sh
python manage.py migrate
```

### 5️⃣ Запуск сервера
```sh
python manage.py runserver
```

## 👤 Доступные тестовые пользователи
После выполнения миграций будут доступны пользователи:

### Суперпользователь:
- **username:** `admin`
- **password:** `adminpassword`

### Тестовый пользователь:
- **username:** `testuser`
- **password:** `testpassword`

А также 10 задач для тестового пользователя.

## 📌 API Эндпоинты

### 🔑 Аутентификация
- `POST /api/users/register/` — регистрация
- `POST /api/users/login/` — вход (получение токенов)
- `POST /api/users/logout/` — выход (блокировка refresh-токена)
- `POST /api/users/token/refresh/` — обновление access-токена

### ✅ Задачи
- `GET /api/tasks/` — список задач (фильтрация по `show_completed`)
- `POST /api/tasks/` — создание задачи
- `GET /api/tasks/{id}/` — получение задачи
- `PUT /api/tasks/{id}/` — обновление задачи
- `DELETE /api/tasks/{id}/` — удаление задачи

## ⚡ Фильтрация задач
Можно передавать `show_completed=true` или `show_completed=false`, чтобы отфильтровать список задач.

```sh
GET /api/tasks/?show_completed=false
```
