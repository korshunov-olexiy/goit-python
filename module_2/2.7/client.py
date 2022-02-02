import socket
from time import sleep


def simple_client(host: str, port: int, timeout: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        attempt = 0
        while attempt < timeout:
            attempt += 1
            try:
                socket.timeout(timeout)
                soc.connect((host, port))
                soc.setblocking(True)
                soc.sendall(input('Input data to send: ').encode())
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
