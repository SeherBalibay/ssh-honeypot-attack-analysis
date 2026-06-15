import socket
import sqlite3
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from geoip.geo_lookup import get_country

HOST = "127.0.0.1"
PORT = 5050
DB_PATH = "../database/attacks.db"


def initialize_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            username TEXT,
            password TEXT,
            country TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            command TEXT NOT NULL
        )
    """)

    try:
        cursor.execute("ALTER TABLE attacks ADD COLUMN country TEXT")
    except sqlite3.OperationalError:
        pass

    connection.commit()
    connection.close()


def save_attack(ip_address, username, password):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    country = get_country(ip_address)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO attacks (timestamp, ip_address, username, password, country)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, ip_address, username, password, country))

    connection.commit()
    connection.close()

    print(f"[+] Attack saved to database | Country: {country}")


def save_command(ip_address, command):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO commands (timestamp, ip_address, command)
        VALUES (?, ?, ?)
    """, (timestamp, ip_address, command))

    connection.commit()
    connection.close()

    print(f"[+] Command saved: {command}")


def fake_shell(client, ip_address):
    client.send(b"\nLogin successful.\n")
    client.send(b"root@ubuntu:~$ ")

    while True:
        command = client.recv(1024).decode(errors="ignore").strip()

        if not command:
            break

        print(f"[COMMAND] {command}")
        save_command(ip_address, command)

        if command == "whoami":
            client.send(b"root\n")

        elif command == "pwd":
            client.send(b"/root\n")

        elif command == "ls":
            client.send(b"passwords.txt\nbackup.tar.gz\nusers.db\n")

        elif command == "cat passwords.txt":
            client.send(b"admin:123456\nroot:toor\n")

        elif command == "uname -a":
            client.send(b"Linux ubuntu 5.15.0-84-generic x86_64 GNU/Linux\n")

        elif command == "exit":
            client.send(b"logout\n")
            break

        else:
            client.send(b"command not found\n")

        client.send(b"root@ubuntu:~$ ")


initialize_database()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(5)

print(f"[+] SSH Honeypot listening on {HOST}:{PORT}")

while True:
    client, address = server.accept()

    ip = address[0]

    print(f"\n[ATTACK] Connection from {ip}")

    client.send(b"Username: ")
    username = client.recv(1024).decode(errors="ignore").strip()

    client.send(b"Password: ")
    password = client.recv(1024).decode(errors="ignore").strip()

    print(f"[USERNAME] {username}")
    print(f"[PASSWORD] {password}")

    save_attack(ip, username, password)

    fake_shell(client, ip)

    client.close()