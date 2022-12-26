import socket

ip = "mention your ip address for client"
port = "mention ur port "

def main():
    sock = socket.socket(socket,AF_INET,SOCK_STREAM)
    address = (ip, port)
    sock.bind(address)
    sock.listen(1)
    conn, ipvictim = sock.accept()
    msg = "this is server"
    conn.send(msg.encode())
    conn.close()


main()
