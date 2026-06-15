import socket
import time

HOST = "127.0.0.1"
PORT = 5050

s = socket.socket()
s.connect((HOST, PORT))

print(s.recv(1024).decode(errors="ignore"))
s.send(b"root\n")
time.sleep(0.2)

print(s.recv(1024).decode(errors="ignore"))
s.send(b"123456\n")
time.sleep(0.2)

print(s.recv(2048).decode(errors="ignore"))

commands = ["whoami", "pwd", "ls", "cat passwords.txt", "uname -a", "exit"]

for command in commands:
    print(f"\n> {command}")
    s.send((command + "\n").encode())
    time.sleep(0.3)
    print(s.recv(4096).decode(errors="ignore"))

s.close()