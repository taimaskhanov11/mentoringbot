Дефолтный бот для оповещения пользователей для записи на интенсивы и тд

Установка на windows

1. установить poetry:
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
2. установить postgres: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
3. поставить пароль postgres


4. установить пакеты проекта: poetry install
5. заполнить данные в config.yaml
6. запустить бота: poetry run python .\mentoring_bot\main.py
