import socket

# Client-side code (UDP)
def start_udp_client():
    # Creating a new socket object that supports TCP over IPv4.
    # AF_INET specifies the address family, in this case, IPv4. 
    # It indicates that the socket will use an IP address.
    # SOCK_DGRAM specifies that the socket will use UDP protocol.
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Since this is UDP, we don't establish any connections

    while True:
        # Send a message to the server
        message = input("You: ")

        # The sendto() method is used to send data to a specific server's port when using UDP.
        # Since UDP is a connectionless protocol, unlike TCP, the server doesn't maintain a 
        # continuous connection with the client. So, the client must specify the target 
        # server's address every time it sends data.
        udp_client_socket.sendto(message.encode(), ("127.0.0.1", 12345))

        # Receive data from the server
        # The recvfrom() method is used to receive data from the server with no specific connection.
        # 1024 specifies the maximum amount of data (in bytes) to be received in one call. 
        # Unlike recv(), recvfrom() provides the server address along with the message
        # The decode() method is called to convert the received byte stream (raw binary data) 
        # into a string format, by default using 'utf-8'
        server_response, _ = udp_client_socket.recvfrom(1024)
        print("Bot:", server_response.decode())

        # This message is used to breakout from the chatbot's conversational loop
        if message == "Goodbye":
            break

    # The close() method for the server socket shuts down the server socket gracefully and 
    # releases any resources associated with it.
    udp_client_socket.close()

if __name__ == "__main__":
    start_udp_client()
