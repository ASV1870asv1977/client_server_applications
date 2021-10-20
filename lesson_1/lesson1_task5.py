"""
Задача № 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
 тип на кириллице.
"""
# ----------------------------------------------------------------------------------------------------------------------
import subprocess
import chardet


def ping_service(service):
    args = ['ping', service]
    ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    count = 0  # Для выхода из режима пингования
    for line in ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
        if count == 4:
            break
        count += 1


if __name__ == '__main__':
    ping_service('yandex.ru')
    ping_service('youtube.com')
