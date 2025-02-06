# DreamBar

## Установка Poetry Windows

Ставим этой командой poetry:
```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
Делаем переменную в системе так:

```shell
Имя переменной Path  

Путь: C:\Users\ИМЯ ПОЛЬЗОВАТЕЛЯ ПК\AppData\Roaming\Python\Scripts
```

## Запуск стартовый  
```shell
poetry install
poetry run python -m manage createsuperuser
poetry run python -m manage runserver
```