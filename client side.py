import socket

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 1442))

# Encode the data to be transmitted into the timestamp field by multiplying it by a fixed value
data = 123
timestamp = (data * 100).to_bytes(4, byteorder='little')

# Build the message to be sent to the server
message = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' + timestamp

# Send the message to the server
client_socket.send(message)

# Close the socket
client_socket.close()
