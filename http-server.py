#Gavin Tank; TO RUN: python http-server.py
import socket
import threading
import sys

serverPort = 6789

def handle_request(connectionSocket):
    try:
        # TODO: Receive and Decode the request
        message = connectionSocket.recv(1024).decode() # Fill in
        if not message:
               print(f"disconnected.")
               return
        
        # TODO: Parse the filename from the message (usually the second part of the first line)
        filename = message.split()[1]
        
        with open(filename[1:], "rb") as f:
            content = f.read()
            
        # TODO: Send HTTP Header (200 OK)
        header = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(header.encode())
        # TODO: Send the content of the requested file
        connectionSocket.send(content)
        
    except IOError:
        # TODO: Send HTTP Header (404 Not Found)
        header = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(header.encode())
        # TODO: Send a basic HTML error message body
        error_message = "<html><body><h1>404 Not Found</h1><p>The file you requested does not exist.</p></body></html>"
        connectionSocket.send(error_message.encode())
        pass
    finally:
        connectionSocket.close()

def start_server():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # TODO: Bind and Listen
    serverSocket.bind(('',serverPort))
    serverSocket.listen(5)
    print(f"[LISTENING] Server is waiting for connections on port {serverPort}...")
    
    while True:
        # TODO: Accept connection and spawn thread
        connectionSocket, addr = serverSocket.accept()
        t = threading.Thread(target=handle_request, args=(connectionSocket,))
        t.start()
        pass

if __name__ == "__main__":
    start_server()
