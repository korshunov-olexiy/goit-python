import socket
import sys
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread
from functools import partial
from time import sleep, time
from typing import Any, Callable, Dict, Iterable, Mapping


class SimpleThread(Thread):
    def __init__(self, targs: Dict) -> None:
        target = targs.get("target", None)
        name = targs.get("name", None)
        args = targs.get("args", ())
        kwargs = targs.get("kwargs", {})
        daemon = targs.get("daemon", True)
        group = None
        super().__init__(group, target, name, args, kwargs, daemon=daemon)


def simple_server(host, port):
    print(f"listening {host}:{port}")
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
                    print(f'From client: {data}')
                elif data == "exit":
                    conn.close()
                    return "exit"

def simple_client(host, port):
    socket.setdefaulttimeout(120.0)
    timeout = 5
    print(f"attempt connect to server {host}:{port}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        try:
            soc.setblocking(False)
            soc.connect_ex((host, port))
        except socket.error:
            sleep(timeout)
            return simple_client(host, port)
        while True:
            send_data = input("::> ").encode("utf8")
            try:
                soc.sendall(send_data)
            except socket.error as error:
                print(f"An error has occurred: {error.errno}: {error.strerror}")
                if send_data == b"exit":
                    return "exit"
                return simple_client(host, port)
            if send_data == b"exit":
                soc.close()
                return "exit"


if __name__ == "__main__":
    try:
        config_file = sys.argv[1]
    except IndexError:
        print("Please specify the name of the configuration file.")
        sys.exit()
    with open(config_file, "r") as f:
        try:
            config_values = map(lambda val: int(val) if val.isdigit() else val, f.read().strip().split(";"))
        except:
            print("Error in configuration file.")
    HOST, PORT_SERVER, PORT_CLIENT = config_values
    # pool = ThreadPool(4)
    # vals = [{"target": simple_server, "args": (HOST, PORT_SERVER)}, {"target": simple_client, "args": (HOST, PORT_CLIENT)}]
    # results = pool.map(SimpleThread, vals)
    res1 = Thread(target=simple_client, args=(HOST, PORT_CLIENT))
    res2 = Thread(target=simple_server, args=(HOST, PORT_SERVER))
    results = (res1, res2)
    for res in results:
        res.start()
    while all([res.is_alive() for res in results]):
        """"""
    # for res in results:
    #     res.join()
    # pool.close()
    # pool.join()
