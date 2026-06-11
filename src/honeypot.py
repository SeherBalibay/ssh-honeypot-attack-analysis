import socket

HOST = "0.0.0.0"
PORT = 2222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(5)

print(f"[+] SSH Honeypot listening on port {PORT}")

while True:
    client, address = server.accept()

    print(f"[ATTACK] Connection received from {address[0]}")

    client.send(b"Fake SSH Service\r\n")

    client.close()