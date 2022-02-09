# -*- coding: utf8 -*-

import socket
import sys
from threading import Thread
from time import sleep
from typing import Any, Callable, Iterable, Mapping


class ThreadWithReturnValue(Thread):
    def __init__(self, group = None, target: Mapping[Callable[..., Any], Any] = None, name: str = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] = None, *, daemon: bool = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self._return = None
    # def __init__(self, group=None, target=None, name=None,
    #              args=(), kwargs={}, Verbose=None):
    #     Thread.__init__(self, group, target, name, args, kwargs, Verbose)
    #    self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        Thread.join(self)
        return self._return


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
                    return "exit"
                # else:
                #     conn.send(data.upper())

def simple_client(host, port):
    with socket.socket() as soc:
        soc.connect((host, port))
        while True:
            try:
                send_data = input("Enter your message:\n").encode("utf8")
                soc.sendall(send_data)
                if send_data == b"exit":
                    soc.close()
                    return "exit"
            except ConnectionRefusedError:
                sleep(0.5)

def run_service_in_thread(func, vals):
    sc = None
    while not sc or sc.join() != "exit":
        if not sc or not sc.is_alive():
            print("begin...")
            sc = ThreadWithReturnValue(target=func, args=vals)
            sc.start()

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
    # server = ThreadWithReturnValue(target=simple_server, args=(HOST, PORT_SERVER))
    # client = ThreadWithReturnValue(target=simple_client, args=(HOST, PORT_CLIENT))
    # server.start()
    # client.start()
    # server.join()
    # client.join()
    run_service_in_thread(simple_client, (HOST, PORT_CLIENT))
    run_service_in_thread(simple_server, (HOST, PORT_SERVER))
    print('Done!')
