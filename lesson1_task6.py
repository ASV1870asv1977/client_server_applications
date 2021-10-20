"""
Задача № 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести
его содержимое.
"""
# ----------------------------------------------------------------------------------------------------------------------
import chardet

string_list = [
    'сетевое программирование',
    'сокет',
    'декоратор',
]

# Запись в файл
with open('task_6.txt', 'w') as f:
    for string in string_list:
        f.write(f'{string}\n')
    print(f'Кодировка по умолчанию: {f}')

# Открытие файла в формате Unicode
with open('task_6.txt', 'rb') as f:
    byte = f.read()
    print(f'Содержимое файла в формате "Unicode": {byte}')
    result = chardet.detect(byte)
    line = byte.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
