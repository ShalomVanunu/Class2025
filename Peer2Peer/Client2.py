import socket


def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the server hostname and port
    host = "172.20.129.108"  # Replace with server IP if needed
    port = 12345

    # Connect to the server
    client_socket.connect((host, port))

    while True:
        # Send a message to the server
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

        # Receive response from the server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {response}")

    client_socket.close()


if __name__ == "__main__":
    start_client()
