import socket

ip = "mention your ip address for client"
port = "mention the connection port"


def main():
     sock = socket.socket(socket,AF_INET,socket.SOCK_STREAM)
     address = (ip, port)
     sock.connect(address)
     msg = sock.recv(1024)
     print(msg.decode())
     sock.close()

main()

