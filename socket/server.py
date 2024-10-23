import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 3000))

sock.listen()

# while True:
conn, address = sock.accept()

# print(address)

msg = conn.recv(1000)
print(msg.decode())

conn.close()
sock.close()


