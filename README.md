# HackLifeBalance
[![linting and unit-testing](https://github.com/Elevator-future/learning-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Elevator-future/learning-platform/actions/workflows/ci.yml)
________________________________________
### Запуск приложения<a name="run"></a>
Заполните файл `.env`
```shell
cp .env.example .env 
```
Установите с помощью менеджера версий pyenv python3.11.6
```shell
pyenv install 3.11.6 && pyenv global 3.11.6
```
С помощью poetry истановите виртуальное окружение и зависимости проекта
```shell
poetry env use python
poetry install
```

Для локальной разработки запустите:
```shell
sudo docker-compose --env-file .env -f infrastructure/docker-compose.local.yaml up --build
python backend/manage.py runserver
```

**_Примечание:_** при локальном запуске, когда часть сервисов работает в контейнере, а основное приложение запущено локально
убедитесь, что в переменных окружения - `.env` вашего локального сервиса `DB_HOST=localhost`.
Это связано с тем, что база данных развернута в контейнере
для нашего сервиса на хосте 127.0.0.1 или **localhost**.
