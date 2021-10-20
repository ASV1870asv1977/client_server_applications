"""
Задача № 2.
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
автоматизирующий его заполнение данными. Для этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;

b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
# ----------------------------------------------------------------------------------------------------------------------
import json


def write_order_to_json(item, quantity, price, buyer, date):
    """
    Функция записи в файл .json по установленной форме.
    :param item: список товаров
    :param quantity: список количества товаров
    :param price: список цен товаров
    :param buyer: список покупателей
    :param date: список дат покупок
    :return: None
    """
    with open('data/orders.json', encoding='utf-8') as f:
        order = json.load(f)

    order_dict = {}
    for num in range(len(item)):
        order_dict['item'] = item[num]
        order_dict['quantity'] = quantity[num]
        order_dict['price'] = price[num]
        order_dict['buyer'] = buyer[num]
        order_dict['date'] = date[num]
        order['orders'].append(order_dict)

    with open('data/orders_data.json', 'w', encoding='utf-8') as f:
        json.dump(order, f, indent=4)


if __name__ == '__main__':

    ITEM = ['Display', 'Printer', 'Mouse']
    QUANTITY = [3, 4, 5]
    PRICE = [10000, 12000, 2000]
    BUYER = ['Ivanov', 'Petrov', 'Sobolev']
    DATE = ['18.10.2021', '19.10.2021', '20.10.20.21']

    write_order_to_json(ITEM, QUANTITY, PRICE, BUYER, DATE)
