import sys
import json
import socket
import time

from common.utils import message_send, accept_message
from lesson_3.common.settings import ACTION, PRESENCE, TIME, DEFAULT_PORT, USER, ACCOUNT_NAME, RESPONSE, ERROR, \
    DEFAULT_IP_ADDRESS


def create_format(account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента
    :param account_name: наименование аккаунта
    :return: формат сообщения
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        'port': DEFAULT_PORT,
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def parsing_answer(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return: код ответа
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    """Загружаем параметры командной строки"""
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_format()
    message_send(transport, message_to_server)
    try:
        answer = parsing_answer(accept_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
