import socket
import GetNameDB

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name and set a port
    host = "172.20.143.77"
    port = 5544

    # Bind the socket to the port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Establish a connection
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")


        # Receive message from client
        code = client_socket.recv(1024).decode('utf-8')
        name = GetNameDB.get_name_by_card_number(code)
        client_socket.send(name.encode())

start_server()