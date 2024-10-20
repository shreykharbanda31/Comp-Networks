import socket

# Server-side code (UDP)
def start_udp_server():
    # Creating a new socket object that supports TCP over IPv4.
    # AF_INET specifies the address family, in this case, IPv4. 
    # It indicates that the socket will use an IP address.
    # SOCK_DGRAM specifies that the socket will use UDP protocol.
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Binding the socket to a specific IP address and port number 
    # It associates the socket with a specific local network interface and port number, 
    # making it available to listen for incoming connections.
    # In this case, the IP address is the loopback address (localhost). 
    # It limits the server to only accept connections from the same machine
    # The port 12345 uniquely identifies the server process running on the local machine.
    udp_server_socket.bind(("127.0.0.1", 12345))
    print("UDP Server up and listening.")

    # Predefining chatbot responses
    chatbot_responses = {
        "Hey": "Hello! How can I help you today?",
        "What's your name?": "It's nice to meet you!",
        "Goodbye": "Goodbye! Talk soon!"
    }

    while True:
        # Receive data from the client
        # The recvfrom() method is used to receive data from the client with no specific connection.
        # 1024 specifies the maximum amount of data (in bytes) to be received in one call. 
        # Unlike recv(), recvfrom() provides the client address along with the message
        # The decode() method is called to convert the received byte stream (raw binary data) 
        # into a string format, by default using 'utf-8'
        message, client_address = udp_server_socket.recvfrom(1024)
        client_message = message.decode()

        # Checks if a response exists in chatbot's dictionary of responses,
        # otherwise, it returns a default message
        response = chatbot_responses.get(client_message, "Sorry, I don't understand.")
        
        # The sendto() method is used to send data to a specific client when using UDP.
        # Since UDP is a connectionless protocol, unlike TCP, the server doesn't maintain a 
        # continuous connection with the client. So, the server must specify the target 
        # client’s address every time it sends data.
        udp_server_socket.sendto(response.encode(), client_address)

        # This message is used to breakout from the chatbot's conversational loop
        if client_message == "Goodbye":
            break

    # The close() method for the server socket shuts down the server socket gracefully and 
    # releases any resources associated with it.
    udp_server_socket.close()

if __name__ == "__main__":
    start_udp_server()
