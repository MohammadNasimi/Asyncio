import socket
ip = '127.0.0.1'
port = 5230
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.bind((ip , port))
tcpSocket.listen(5)


while True:
    client, addr = tcpSocket.accept()
    print("Got connection from", addr)
    client.send(b"thank you for connecting")
    client.close()