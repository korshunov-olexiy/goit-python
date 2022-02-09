# -*- coding: utf8 -*-
import socket
from time import sleep
import sys

from time import sleep

def simple_client(host, port):
    socket.setdefaulttimeout(120.0)
    with socket.socket() as soc:
        soc.connect((host, port))
        # soc.setblocking(False)
        while True:
            try:
                send_data = input("Enter your message to send: ").encode("utf8")
                soc.sendall(send_data)
                if send_data == b"exit":
                    soc.close()
                    break
                else:
                    data = soc.recv(1024).decode("utf8")
                    print(f'From server: {data}')
            except ConnectionRefusedError:
                sleep(0.5)


if __name__ == "__main__":
    host, port = "127.0.0.1", 9080
    simple_client(host, port)
