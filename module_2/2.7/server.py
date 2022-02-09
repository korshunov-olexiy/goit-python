# -*- coding: utf8 -*-

import socket
import sys
from datetime import datetime

def simple_server(host, port):
    with socket.socket() as soc:
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.bind((host, port))
        soc.listen(1)
        conn, addr = soc.accept()
        current_datetime = datetime.today().strftime("%d.%m.%y %H:%M:%S")
        print(f'{current_datetime}. Connected by {addr}')
        with conn:
            while True:
                data = conn.recv(1024).decode("utf8")
                current_datetime = datetime.today().strftime("%d.%m.%y %H:%M:%S")
                print(f'{current_datetime}. From client:\n{data}')
                if data == "exit":
                    print(f'Exit command received. Shutdown server...')
                    conn.close()
                    break
                else:
                    send_data = input("Enter your message to send:\n").encode("utf8")
                    if send_data:
                        conn.send(send_data)


if __name__ == "__main__":
    host, port = "127.0.0.1", 9080
    simple_server(host, port)
