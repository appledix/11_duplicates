# 11_duplicates

## Описание

Данный скрипт находит дублирующие друг друга файлы в дереве переданной ему директории.
Для работы необходимо вызвать скрипт через терминал с директорией для обхода в качестве аргумента. 
После запуска скрипт рекурсивно пройдётся по всему содержимому заданного каталога и выведет в терминал названия неоднократно повторяющихся файлов и их местоположение, возлагая на плечи пользователя решение об их дальнейшей судьбе.

## Использование
Запуск через терминал, при помощи python 3:

    python3.5 duplicates.py <directory>
  