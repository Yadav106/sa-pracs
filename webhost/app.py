import socket

HOST = "127.0.0.1"
PORT = int(input("Enter port number : "))

html_code = ""
with open("index.html", "r") as html_file:
    html_code = html_file.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_stream:
    socket_stream.bind((HOST, PORT))

    socket_stream.listen()

    print(f"Listening on port {PORT}")

    while True:
        conn, addr = socket_stream.accept()

        print(f"Connected from {addr}")

        with conn:
            request = conn.recv(1024).decode()

            print(request)

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(html_code)}\r\n"
                "Connection: close\r\n"
                "\r\n" +
                html_code
            )

            conn.sendall(response.encode())
    
