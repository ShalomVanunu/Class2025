import socket
import threading


def handle_client(client_socket, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Client {addr}: {message}")

            # Send a response back to the client
            response = input(f"You (from {addr}): ")
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Error with client {addr}: {e}")
            break

    client_socket.close()
    print(f"Connection with {addr} closed.")


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name and set a port
    host = "172.20.130.119"
    port = 12345

    # Bind the socket to the port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()


if __name__ == "__main__":
    start_server()
