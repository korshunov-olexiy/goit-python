import socket
import sys
from time import sleep
from threading import Event, Thread


class Manager:

    def __init__(self, host: str, port_server: int, port_client: int) -> None:
        self.host, self.port_server, self.port_client = host, port_server, port_client
        self._stop_event = Event()
        thread1 = Thread(target=self.simple_server, daemon=True)
        thread1.start()
        thread2 = Thread(target=self.simple_client, daemon=True)
        thread2.start()
        self.check_stopped()

    def simple_server(self):
        print(f"listening {self.host}:{self.port_server}")
        with socket.socket() as soc:
            soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            soc.bind((self.host, self.port_server))
            soc.listen(1)
            conn, addr = soc.accept()
            print(f"Connected by {addr}")
            data = None
            with conn:
                while True:
                    try:
                        data = conn.recv(1024).decode("utf8")
                    except (ConnectionResetError, ConnectionRefusedError):
                        conn.close()
                        self.stop()
                        break
                    if data:
                        if data == "exit":
                            conn.close()
                            self.stop()
                            break
                        print(f'From client: {data}')

    def simple_client(self):
        timeout = 5
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            try:
                soc.connect((self.host, self.port_client))
            except socket.error as error:
                sleep(timeout)
                self.simple_client()
            while True:
                send_data = input("::> ").encode("utf8")
                try:
                    soc.sendall(send_data)
                except socket.error as error:
                    print(f"An error has occurred: {error.errno}: {error.strerror}")
                    if send_data == b"exit":
                        soc.close()
                        self.stop()
                        return None
                    self.simple_client()
                if send_data == b"exit":
                    soc.close()
                    self.stop()
                    return None

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def check_stopped(self):
        while True:
            if self.stopped():
                print("Shutdown messanger. Goodbye...")
                sys.exit()
            sleep(1)


if __name__ == '__main__':
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
    Manager(HOST, PORT_SERVER, PORT_CLIENT)
