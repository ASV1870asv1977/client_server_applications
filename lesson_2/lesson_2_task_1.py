"""
Задача № 1.
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить
в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;

c. Проверить работу программы через вызов функции write_to_csv().
"""
# ----------------------------------------------------------------------------------------------------------------------
import csv
import chardet

FIELD_LIST = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
PATH = 'data/main_data.csv'


def get_data():
    """
    Функция считывает данные из файлов .txt, формирует четыре списка из отфильтрованных значений по FIELD_LIST,
    создает главный список для хранения списка столбцов отчета и списков отфильтрованных значений, записывает его
    в .csv файл.
    :return: None
    """
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for num in range(1, 4):
        with open(f'data/info_{num}.txt', 'rb') as f:
            for row in f:
                result = chardet.detect(row)
                row = row.decode(result['encoding']).encode('utf-8')
                row = row.decode('utf-8').rstrip('\r\n')
                list_row = row.split(':')

                if len(list_row) > 1:
                    temp = list_row[1].split(' ')
                    temp = [item for item in temp if item]
                    temp = ' '.join(temp)
                # Взят срез из-за некорректного декодирования начальных букв строки
                if list_row[0][2:] in FIELD_LIST[0]:
                    os_prod_list.append(temp)
                elif list_row[0][2:] in FIELD_LIST[1]:
                    os_name_list.append(temp)
                elif list_row[0][2:] in FIELD_LIST[2]:
                    os_code_list.append(temp)
                elif list_row[0][2:] in FIELD_LIST[3]:
                    os_type_list.append(temp)

    main_data = [FIELD_LIST, os_prod_list, os_name_list, os_code_list, os_type_list]

    with open(PATH, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(main_data)


def write_to_csv(path):
    """
    Функция считывает данные из файла .csv с исходными данными. Переформирует список представления. Записывает список
    представления в .csv файл.
    :param path: Путь к файлу с исходными данными
    :return: None
    """
    get_data()
    write_list = []
    with open(path, 'r') as f:
        temp_reader = csv.reader(f)
        headers = next(temp_reader)
        data_list = [row for row in temp_reader]
    write_list.append(headers)
    data_list = list(zip(data_list[0], data_list[1], data_list[2], data_list[3]))
    for item in data_list:
        write_list.append(list(item))

    with open(f'data/order_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(write_list)


if __name__ == '__main__':
    write_to_csv(PATH)


"""
Задача выполнена, как поставлена. ТЗ в большинстве своем непонятно.
"""
