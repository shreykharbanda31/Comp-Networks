import socket

# Client-side code (TCP)
def start_tcp_client():
    # Creating a new socket object that supports TCP over IPv4.
    # AF_INET specifies the address family, in this case, IPv4. 
    # It indicates that the socket will use an IP address.
    # SOCK_STREAM specifies that the socket will use TCP protocol.
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # It attempts to establish a connection between the client socket and a server running 
    # on the local machine (localhost) at port 12345.
    tcp_client_socket.connect(("127.0.0.1", 12345))

    while True:
        # Send a message to the server
        message = input("You: ")
        # The send() method is used to send data to the server through the connection 
        # It sends the data as an encoded byte stream, instead of a string, by default
        # 'utf-8'
        tcp_client_socket.send(message.encode())

         # The recv() method is used to receive data from the server through the connection.
        # 1024 specifies the maximum amount of data (in bytes) to be received in one call. 
        # The decode() method is called to convert the received byte stream (raw binary data) 
        # into a string format, by default using 'utf-8'
        server_response = tcp_client_socket.recv(1024).decode()
        print("Bot:", server_response)
        
        # This message is used to breakout from the chatbot's conversational loop
        if message == "Goodbye":
            break
    
    # The close() method for the client socket closes the connection with the server.
    tcp_client_socket.close()

if __name__ == "__main__":
    start_tcp_client()
