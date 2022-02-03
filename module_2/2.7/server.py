# -*- coding: utf8 -*-

import socket
import sys

def echo_server(host, port):
    with socket.socket() as soc:
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.bind((host, port))
        soc.listen()
        conn, addr = soc.accept()
        print(f"Connected by {addr}")
        with conn:
            print("wait size of data...")
            size_msg = conn.recv(1024)
            print(size_msg.decode("utf8"))
            # data = conn.recv(int(size_msg))
            # print(f"Size: {sys.getsizeof(data)}, msg: {data.decode('utf8')}")
            conn.sendall(str.encode("ok"))


if __name__ == "__main__":
    host, port = "", 9090
    echo_server(host, port)
