"""
Задача № 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""
# ----------------------------------------------------------------------------------------------------------------------
from urllib3.packages.six import b


string_list = [
    'attribute',
    'класс',
    'функция',
    'type',
]

for string in string_list:
    try:
        byte = b(string)
        print(f'Тип: {type(byte)}, Содержимое: {byte}')
    except UnicodeEncodeError:
        print(f'строку "{string}" из символов не относящихся к ASCII(кириллица) невозможно записать в байтовом типе')
