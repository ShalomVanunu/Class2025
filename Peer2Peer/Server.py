import socket


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name and set a port
    host = "172.20.129.108"
    port = 12345

    # Bind the socket to the port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Establish a connection
    client_socket, addr = server_socket.accept()
    print(client_socket)
    print(f"Got a connection from {addr}")

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Client: {message}")

        # Send a response back to the client
        response = input("You: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
