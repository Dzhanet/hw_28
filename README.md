## Проект готов к локальному запуску

Запустить базу данных c postgres:  docker-compose up -d

## Для начала проекта с нуля
1) Удалить том postgres (pg_data)
2) Удалить миграции из приложений (пользователи, реклама)
3) Запустить базу данных postgres docker-compose up -d

### Миграции
- Создать миграции:

./manage.py makemagrations

------------------
- Накатить миграцию:

./manage.py migrate

### Загрузка данных в БД :

- ./manage.py loaddata location.json
- ./manage.py loaddata user.json
- ./manage.py loaddata category.json
- ./manage.py loaddata ad.json

### Для доступа к админке

- Админ: skypro
- пароль: 1234

PS: 
user/
user/total_ads/ - Доступен только для Админа
