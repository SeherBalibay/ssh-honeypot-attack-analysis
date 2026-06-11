import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(5)

print(f"[+] SSH Honeypot listening on port {PORT}")

while True:
    client, address = server.accept()

    ip = address[0]
    timestamp = datetime.now()

    print(f"\n[ATTACK] Connection from {ip}")
    print(f"[TIME] {timestamp}")

    client.send(b"Username: ")

    username = client.recv(1024).decode().strip()

    client.send(b"Password: ")

    password = client.recv(1024).decode().strip()

    print(f"[USERNAME] {username}")
    print(f"[PASSWORD] {password}")

    with open("attack_logs.txt", "a", encoding="utf-8") as log:
        log.write(
            f"{timestamp} | IP:{ip} | USER:{username} | PASS:{password}\n"
        )

    client.close()