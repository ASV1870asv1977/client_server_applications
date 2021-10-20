"""
Задача № 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип
и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представления
в формат Unicode и также проверить тип и содержимое переменных.
"""
# ----------------------------------------------------------------------------------------------------------------------


string_list = [
    'разработка',
    'сокет',
    'декоратор'
]

# Преставление в строковом формате и проверка типа и содержания соответствующих переменных
for string in string_list:
    print(type(string), string)

byte_list = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

# Преставление в формате Unicode и проверка типа и содержания соответствующих переменных
for byte in byte_list:
    print(type(byte), byte)
