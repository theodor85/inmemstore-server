## In-memory key-value хранилище (сервер)

Хранит в оперативной памяти пары ключ-значение.

## Установка

Клонировать репозиторий:

```
git clone https://github.com/theodor85/inmemstore-server.git
cd inmemstore-server
```

Создать и активировать виртуальное окружение любым способом, например (для Ubuntu):

```
python3 -m venv env
source ./env/bin/actuvate
```

Установить зависимости:

```
pip install -r requirements.txt
```

## Запуск

```
python main.py
```

## Запуск тестов

После запуска сервера, можно запустить тесты в другом терминале (необходимо активировать то же самое виртуальное окружение, что для сервера)

```
pytest ./tests/tests.py
```
