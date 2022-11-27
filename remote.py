import time
import socket
import sys
import os

soc = socket.socket()
host = socket.gethostname()
port = 8080
soc.bind(('', port))

print("waiting for connections...")
soc.listen()
conn, addr = soc.accept()

print(addr, "is connected to server")
command = input(str("Enter Command :"))
conn.send(command.encode())
print("Command has been sent successfully.")
data = conn.recv(1024)

if data:
   print("command received and executed successfully.")
   
   soc = socket.socket()
host = "127.0.0.1”
port = 8080
soc.connect((host, port))
print("Connected to Server.")
command = soc.recv(1024)
command = command.decode()
if command == "open":
    print("Command is :", command)
    soc.send("Command received".encode())
    os.system('test.bat')
