#Gavin Tank; TO RUN: python client.py <localhost> <6789> <filename>
from socket import *
import sys

def start_client():
    if len(sys.argv) < 4:
        print("Usage: python client.py <server_host> <server_port> <filename>")
        return
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server_host,server_port))
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    clientSocket.send(request.encode())
    print("--- Raw Server Response ---")
    while True:
        data = clientSocket.recv(4096)
        if not data:
            break
        print(data.decode(), end='')

    clientSocket.close()

if __name__ == "__main__":
    start_client()