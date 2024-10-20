import socket

# Server-side code (TCP)
def start_tcp_server():
    # Creating a new socket object that supports TCP over IPv4.
    # AF_INET specifies the address family, in this case, IPv4. 
    # It indicates that the socket will use an IP address.
    # SOCK_STREAM specifies that the socket will use TCP protocol.
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding the socket to a specific IP address and port number 
    # It associates the socket with a specific local network interface and port number, 
    # making it available to listen for incoming connections.
    # In this case, the IP address is the loopback address (localhost). 
    # It limits the server to only accept connections from the same machine
    # The port 12345 uniquely identifies the server process running on the local machine.
    tcp_server_socket.bind(("127.0.0.1", 12345))
    # This tells the socket to listen for incoming connections. The argument 1 specifies 
    # the backlog or the maximum number of queued connections before the server starts refusing new ones. 
    # If 1 connection is waiting and another client tries to connect, 
    # it will be refused until the previous connection is handled or the queue is cleared.
    tcp_server_socket.listen(1)
    print(f"TCP Server up at {tcp_server_socket.getsockname()} and listening.")

    # Predefining chatbot responses
    chatbot_responses = {
        "Hey": "Hello! How can I help you today?",
        "What's your name?": "It's nice to meet you!",
        "Goodbye": "Goodbye! Talk soon!"
    }

    # Waiting for client connections and handling them where 
    # conn is the new socket object or the active connection that tcp maintains as a
    # connection-oriented protocol
    conn, client_address = tcp_server_socket.accept()
    print(f"Connected to {client_address}")

    while True:
        # The recv() method is used to receive data from the client through the connection.
        # 1024 specifies the maximum amount of data (in bytes) to be received in one call. 
        # The decode() method is called to convert the received byte stream (raw binary data) 
        # into a string format, by default using 'utf-8'
        client_message = conn.recv(1024).decode()
        # Checks if a response exists in chatbot's dictionary of responses,
        # otherwise, it returns a default message
        response = chatbot_responses.get(client_message, "Sorry, I don't understand.")
        # Sends the response back to the client as an encoded byte stream, instead of a string
        conn.send(response.encode())

        # This message is used to breakout from the chatbot's conversational loop
        if client_message == "Goodbye":
            break

    # The close() method for conn closes the connection with the client. This means that no further data can
    # be sent or received using this socket. It frees up resources associated with this specific connection. 
    conn.close()
    # The close() method for the server socket shuts down the server socket, meaning it will stop listening 
    # for new client connections.
    tcp_server_socket.close()

if __name__ == "__main__":
    start_tcp_server()
