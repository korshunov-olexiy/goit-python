# -*- coding: utf8 -*-
import socket
from time import sleep
import sys

def simple_client(host: str, port: int, timeout: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        attempt = 0
        while attempt < timeout:
            attempt += 1
            try:
                socket.timeout(timeout)
                soc.connect((host, port))
                soc.setblocking(True)
                # soc.sendall(input('Input data to send: ').encode())
                msg  = "Тотал Коммандер – удобное и функциональное приложение, которое облегчит работу с файловой системой компьютера. Эта программа настолько проста в пользовании, что считается гениальной! Она еще больше упрощает работу с ПК. Перед вами открываются новые возможности, такие как просмотр скрытых папок, умный поиск внутри файлов, анализ дисков на наличие дубликатов документов, аудиофайлов и прочего и т. д. И все это вы можете получить бесплатно. Настройка Total Commander – это во многом индивидуальный процесс. Наверное, вы как многие любители подобных программ после установки приложения сразу отправляетесь в файл или в меню с конфигурациями, чтобы увидеть, какие есть функции, и что можно изменить. Так вот, Тотал Коммандер понравится вам еще больше, когда вы увидите безграничное количество опций, которые можно настроить внутри программы! А данная статья вам покажет, как это можно сделать?".encode()
                size_msg = str.encode(str(sys.getsizeof(msg)))
                soc.sendall(size_msg)
                soc.sendall(msg)
                data_recv = soc.recv(1024).decode("utf8")
                if data_recv.upper() != "OK":
                    print("Couldn't deliver your message. The server may have been shut down.")
                else:
                    print("Your message has been delivered. Finishing work.")
                break
            except ConnectionRefusedError:
                sleep(0.5)
        if attempt == timeout:
            print("Could not connect to the server. The server may have been shut down.")

if __name__ == "__main__":
    host, port = "127.0.0.1", 9090
    simple_client(host, port, 3)
