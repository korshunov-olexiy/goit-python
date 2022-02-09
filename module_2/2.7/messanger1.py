# -*- coding: utf8 -*-

import socket
import sys
import threading
from time import sleep


def simple_server(host, port):
    with socket.socket() as soc:
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.bind((host, port))
        soc.listen(1)
        conn, addr = soc.accept()
        print(f"Connected by {addr}")
        with conn:
            while True:
                data = conn.recv(1024).decode("utf8")
                if data:
                    print(f'From client:\n{data}')
                elif data == "exit":
                    conn.close()
                    sys.exit()
                # else:
                #     conn.send(data.upper())

def simple_client(host, port):
    with socket.socket() as soc:
        soc.connect((host, port))
        while True:
            try:
                send_data = input("Enter your message:\n").encode("utf8")
                soc.sendall(send_data)
                # data = soc.recv(1024)
                # print(f'From server: {data}')
                if send_data == b"exit":
                    soc.close()
                    sys.exit()
            except ConnectionRefusedError:
                sleep(0.5)


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT_SERVER, PORT_CLIENT = 9080, 9070
    server = threading.Thread(target=simple_server, args=(HOST, PORT_SERVER))
    client = threading.Thread(target=simple_client, args=(HOST, PORT_CLIENT))
    server.start()
    client.start()
    server.join()
    client.join()
    print('Done!')
