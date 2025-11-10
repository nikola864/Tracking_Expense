# Tracking_Expense

🚀 Описание проекта
Expense Tracker — это веб-приложение для отслеживания личных финансов:
✅ Добавление доходов и расходов
✅ Группировка по категориям (еда, транспорт, зарплата и т.д.)
✅ Автоматический расчёт баланса
✅ Отчёты по категориям за выбранный период
✅ Экспорт данных в CSV
✅ Удобный веб-интерфейс на HTML + JavaScript

Проект создан на FastAPI с использованием SQLAlchemy ORM, Jinja2 для рендеринга HTML и Alembic для управления миграциями базы данных. Подходит для портфолио, фриланса и изучения backend-разработки.

🛠️ Технологии
Python 3.10+
FastAPI — современный фреймворк для API
SQLAlchemy ORM — работа с базой данных
SQLite — локальная БД (можно заменить на PostgreSQL)
Jinja2 — рендеринг HTML-шаблонов
Alembic — управление миграциями
Pydantic — валидация данных
Uvicorn — ASGI-сервер

📂 Структура проекта
expense-tracker/
├── tracking/
│   ├── __init__.py
│   ├── main.py              # FastAPI-приложение
│   ├── models.py            # SQLAlchemy-модели
│   ├── schemas.py           # Pydantic-схемы
│   ├── database.py          # Подключение к БД
│   ├── crud.py              # Операции с БД (CRUD)
│   ├── reports.py           # Логика отчётов
│   └── utils.py             # Экспорт в CSV
├── templates/
│   └── index.html           # Веб-интерфейс
├── alembic/                 # Миграции базы данных
├── exports/                 # Файлы CSV (создаются при экспорте)
├── requirements.txt         # Зависимости
└── README.md
