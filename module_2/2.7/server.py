import socket


def echo_server(host, port):
    with socket.socket() as soc:
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.bind((host, port))
        soc.listen()
        # conn, addr = soc.accept()
        # print(f"Connected by {addr}")
        # with conn:
        #     while True:
        #         # data = conn.recv(1024)
        #         data, client = conn.recvfrom(1024)
        #         if not data:
        #             break
        #         print(f'From client: {data.decode("utf8")}')
        #         # conn.sendto(str.encode("ok"), addr)
        #         # conn.send(str.encode("ok"))
        #         soc.sendto(str.encode("ok"), client)

        con, addr = soc.accept()
        with con:
            data, client = soc.recvfrom(1024)
            # if not data:
            #     break
            print(f"From {client}: {data.decode('utf8')}")
            soc.sendto(str.encode("ok"), client)


if __name__ == "__main__":
    host, port = "", 9090
    echo_server(host, port)
