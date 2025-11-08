### 13) UDP Socket Programming

A **socket** is an endpoint for network communication. You can think of it as a software abstraction of a physical port on a machine, identified by an IP address and a port number. Programming with sockets allows you to send and receive data across a network.

This section focuses on **UDP (User Datagram Protocol)** sockets.

#### Understanding UDP vs. TCP

First, it's essential to know why you would choose UDP.

- **TCP (Transmission Control Protocol):** Is **connection-oriented**. It establishes a reliable, three-way handshake before sending data. It guarantees that packets are delivered in order and without errors (it handles re-transmission). Think of it like a phone call, where you establish a connection and have a continuous conversation.
- **UDP (User Datagram Protocol):** Is **connectionless**. It is a "fire-and-forget" protocol. You simply send a packet (called a datagram) to a destination without establishing a connection first.
  - **Unreliable:** There is no guarantee of delivery or that datagrams will arrive in the order they were sent.
  - **Lightweight and Fast:** It has very low overhead because it doesn't manage connections or re-transmissions. This makes it ideal for speed-sensitive applications where losing an occasional packet is acceptable.

**Common Use Cases for UDP:**

- **DNS:** A quick query and response is more important than guaranteed delivery.
- **Online Gaming:** Sending frequent position updates where the latest data is more important than old, delayed data.
- **Video/Audio Streaming & VoIP:** Speed is critical, and re-transmitting a lost packet of audio from a moment ago would be useless.

---

### Python Program for a Simple UDP Client-Server Chat

We will write two Python scripts: a server that listens for messages and a client that sends them.

**Prerequisites:**

- Python installed on your machine.
- You will need two terminal windows to run the server and the client simultaneously.

#### A) The UDP Server (`udp_server.py`)

The server's job is to:

1.  Create a UDP socket.
2.  **Bind** it to a specific IP address and port, effectively "opening the line" to listen for data.
3.  Enter a loop to continuously wait for incoming datagrams.
4.  When a datagram arrives, print its content and the address of the client who sent it.
5.  Send a response back to that client's address.

````python
# udp_server.py
import socket

# --- Configuration ---
SERVER_IP = "127.0.0.1"  # Listen on localhost (this machine)
SERVER_PORT = 12345
BUFFER_SIZE = 1024       # Max size of a datagram to receive

# 1. Create a UDP socket
#    AF_INET is for IPv4
#    SOCK_DGRAM is for UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind the socket to the IP address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"UDP server is up and listening on {SERVER_IP}:{SERVER_PORT}")

# 3. Listen for incoming datagrams in a loop
while True:
    # recvfrom() blocks until it receives a datagram.
    # It returns the data AND the address (IP, port) of the client that sent it.
    message_bytes, client_address = server_socket.recvfrom(BUFFER_SIZE)

    # Decode the received bytes into a string
    message_str = message_bytes.decode()

    print(f"Message from {client_address}: '{message_str}'")

    # 5. Send a response back to the client
    response = f"Server acknowledges: {message_str}"
    # Encode the string response into bytes to send it
    response_bytes = response.encode()

    # Use sendto() to send the data to the specific client address
    server_socket.sendto(response_bytes, client_address)```

#### B) The UDP Client (`udp_client.py`)

The client's job is to:
1.  Create a UDP socket. (It does *not* need to bind, the OS will assign a random port for it).
2.  Take a message from the user.
3.  **Send** that message to the server's specific IP and port.
4.  Wait to receive a response from the server.

```python
# udp_client.py
import socket

# --- Configuration ---
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345
BUFFER_SIZE = 1024

# 1. Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get a message from the user
message_to_send = input("Enter a message to send to the server: ")

# Encode the message into bytes
message_bytes = message_to_send.encode()

# 3. Send the message to the server using sendto()
try:
    print(f"Sending '{message_to_send}' to {SERVER_IP}:{SERVER_PORT}")
    client_socket.sendto(message_bytes, (SERVER_IP, SERVER_PORT))

    # 4. Wait for a response from the server
    print("Waiting for server response...")
    response_bytes, server_address = client_socket.recvfrom(BUFFER_SIZE)

    response_str = response_bytes.decode()
    print(f"Response from server {server_address}: '{response_str}'")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the socket when done
    client_socket.close()
    print("Socket closed.")
````

---

### How to Run the Simulation

1.  **Save the Code:** Save the two code blocks into files named `udp_server.py` and `udp_client.py`.
2.  **Open Terminal 1 (Server):**
    - Navigate to the directory where you saved the files.
    - Run the server: `python udp_server.py`
    - You will see the message: `UDP server is up and listening...` The server is now waiting.
3.  **Open Terminal 2 (Client):**
    - Navigate to the same directory.
    - Run the client: `python udp_client.py`
4.  **Interact:**
    - The client terminal will prompt you: `Enter a message to send to the server:`. Type `Hello UDP!` and press Enter.
    - **In the client terminal**, you will see it send the message and then receive the server's acknowledgment.
    - **In the server terminal**, you will see it print the message it received from the client.
    - The client will exit, but the server will continue running, ready to accept another message from a new client instance. You can stop the server by pressing `Ctrl + C`.
