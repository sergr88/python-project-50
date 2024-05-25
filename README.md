# Вычислитель отличий

#### Бейджики Hexlet
[![Actions Status](https://github.com/sergr88/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/sergr88/python-project-50/actions)
[![Python CI](https://github.com/sergr88/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/sergr88/python-project-50/actions)
#### Бейджики Code Climate
[![Maintainability](https://api.codeclimate.com/v1/badges/98bd89424bd01882aa2b/maintainability)](https://codeclimate.com/github/sergr88/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/98bd89424bd01882aa2b/test_coverage)](https://codeclimate.com/github/sergr88/python-project-50/test_coverage)

## Описание
Утилита сравнивает два файла в форматах JSON или YAML и выводит различия в
текстовом виде в различных форматах. Примеры работы:
- Вывод справки о параметрах запуска утилиты:
  [![asciicast](https://asciinema.org/a/661126.svg)](https://asciinema.org/a/661126)
- Сравнение плоских JSON-файлов с выводом в стилизованном формате:
  [![asciicast](https://asciinema.org/a/661127.svg)](https://asciinema.org/a/661127)
- Сравнение плоских YAML-файлов с выводом в стилизованном формате:
  [![asciicast](https://asciinema.org/a/661128.svg)](https://asciinema.org/a/661128)
- Сравнение иерархических JSON-файлов с выводом в стилизованном формате:
  [![asciicast](https://asciinema.org/a/661129.svg)](https://asciinema.org/a/661129)
- Сравнение иерархических JSON-файлов с выводом в плоском формате:
  [![asciicast](https://asciinema.org/a/661130.svg)](https://asciinema.org/a/661130)
- Сравнение иерархических JSON-файлов с выводом в JSON-формате:
  [![asciicast](https://asciinema.org/a/661131.svg)](https://asciinema.org/a/661131)

## Требования
- Python 3.11+

## Команды
#### Развертывание
```shell
make install
```
#### Проверка линтером
```shell
make lint
```
#### Выполнение тестов
```shell
make test
```
#### Выполнение тестов с определением покрытия по тестируемым файлам
```shell
make test-coverage
```
#### Выполнение тестов с определением покрытия по всем файлам
```shell
make test-coverage-all
```
