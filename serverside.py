import socket

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Ip of host\n")
port = input("input port number \n")
# Bind to a port and listen for incoming connections
server_socket.bind((host, port))
server_socket.listen(1)

# Accept the incoming connection
connection, address = server_socket.accept()

# Receive the message from the client
message = connection.recv(1024)

# Extract the timestamp field from the TCP header
timestamp = message[36:40]

# Decode the data from the timestamp field by dividing the timestamp by a fixed value
data = int.from_bytes(timestamp, byteorder='little')

# Print the decoded data
print(data)

# Close the connection
connection.close()
