---

### **UNIT-IV: Transport Layer**

The Transport Layer is the engine room of the network model. Its main job is to provide logical communication between **applications** running on different hosts. While the Network Layer gets packets from one computer to another, the Transport Layer gets the data to the correct **process** (application) on that computer.

*   **Process to Process Communication:** This is the core function of the Transport Layer. An IP address gets a packet to the right computer, but that computer might be running a web browser, an email client, and a game all at once. The Transport Layer uses **port numbers** to ensure the data for the web browser goes only to the browser and not the email client. The combination of an IP address and a port number creates a **socket**.

*   **Socket Programming:** A socket is a programming interface (an API) that allows applications to use the network. It's an endpoint for communication, identified by an IP address and a port number. Programmers use functions like `connect()`, `bind()`, `send()`, and `receive()` to create and manage these sockets, enabling applications to talk to each other.

*   **Elements of transport layer protocol:** These are the key services that a transport protocol can offer:
    *   **Addressing (Port Numbers):** Directing data to the correct application on a host.
    *   **Connection Control:** Establishing, managing, and terminating a connection (primarily for TCP).
    *   **Flow Control:** Preventing a fast sender from overwhelming a slow receiver.
    *   **Error Control:** Detecting corrupted packets (using checksums) and managing lost packets (using acknowledgments and retransmissions).
    *   **Congestion Control:** Managing network traffic to prevent the entire network from collapsing due to too much data.

*   **User Datagram Protocol (UDP):**
    *   **Analogy:** Sending a postcard.
    *   A simple, "fire-and-forget" protocol. It is **connectionless** (no handshake required) and **unreliable** (no guarantee of delivery, order, or error correction).
    *   Its advantage is its extremely low overhead, making it very fast.
    *   **Used for:** DNS, VoIP, online gaming, and live streaming, where speed is more critical than perfect reliability.

*   **Transmission Control Protocol (TCP):**
    *   **Analogy:** A phone call.
    *   A reliable, **connection-oriented** protocol. It establishes a connection using a **three-way handshake** (SYN, SYN-ACK, ACK) before any data is sent.
    *   It provides reliability through sequence numbers, acknowledgments, flow control (sliding window), and error detection. It guarantees that data arrives in order and without corruption.
    *   **Used for:** Web browsing (HTTP/HTTPS), email (SMTP), and file transfer (FTP), where data integrity is essential.

*   **SCTP (Stream Control Transmission Protocol):** A more advanced protocol that combines features of both TCP and UDP. Its key features are **multi-streaming** (allows multiple independent data streams within a single connection, preventing one blocked stream from stopping others) and **multi-homing** (can use multiple IP addresses on each side for redundancy). It is primarily used in telecommunications signaling.

*   **Congestion Control:** A mechanism to prevent the network from getting overloaded. If a router starts dropping packets because its buffers are full, TCP assumes the network is congested and slows down its sending rate. This is different from flow control, which is about protecting the receiver; congestion control is about protecting the network itself.

*   **Quality of Service (QoS):** Not all network traffic is equal. A video call is more sensitive to delay than an email. QoS is a set of technologies that manage network resources to provide different levels of priority to different types of traffic, ensuring that critical applications perform as needed.

*   **QoS Improving Techniques - Leaky Bucket and Token Bucket Algorithms:**
    *   **Leaky Bucket:** An algorithm for traffic shaping. It takes bursty, irregular traffic and forces it into a smooth, constant-rate output stream. Any traffic that arrives when the "bucket" (buffer) is full is discarded. This provides a very predictable output but can add delay.
    *   **Token Bucket:** A more flexible algorithm. To send a packet, you must have a "token." Tokens are generated at a constant rate. This allows an application to save up tokens and send a burst of traffic when needed, as long as the long-term average rate is maintained.

*   **Differentiated Services (DiffServ):** A practical method for implementing QoS. It works by marking packets in the IP header with a specific priority level (a DSCP value). Routers along the path can then use this marking to give higher priority to more important packets.

*   **TCP and UDP for Wireless networks:** Wireless networks are prone to packet loss from interference, not just congestion. Standard TCP mistakenly interprets this loss as congestion and slows down unnecessarily. This is a significant performance problem, and specialized versions and optimizations have been developed to improve TCP/UDP performance over wireless links.

---

### **UNIT-V: Application Layer**

This layer is where users and applications interact with the network. It provides the protocols that applications use to communicate.

*   **DNS (Domain Name System):** The "phonebook of the internet." It translates human-readable domain names (e.g., `www.google.com`) into machine-readable IP addresses (e.g., `172.217.167.78`). Uses UDP Port 53.
*   **DDNS (Dynamic DNS):** An service that automatically updates DNS records when the IP address of a host changes. This is useful for home users with dynamic IPs who want to run a server.
*   **TELNET:** An old protocol for providing a remote command-line interface. It is **insecure** because it transmits all data, including passwords, in clear text. Uses TCP Port 23. (SSH on Port 22 is its secure replacement).
*   **EMAIL:** A system composed of several protocols:
    *   **SMTP (Simple Mail Transfer Protocol):** Used for **sending** email from a client to a server and between servers. Uses TCP Port 25.
    *   **POP3/IMAP:** Used for **retrieving** email. POP3 downloads emails to the client (often deleting them from the server), while IMAP synchronizes emails with the server, allowing access from multiple devices.
*   **FTP (File Transfer Protocol):** A protocol for transferring files. It famously uses two separate connections: a **control connection** (Port 21) for commands and a **data connection** (Port 20) for the actual file transfer. It is also insecure.
*   **WWW (World Wide Web):** The system of interconnected hypertext documents accessible via the internet. It is an information space, not a protocol itself.
*   **HTTP (Hypertext Transfer Protocol):** The protocol of the WWW. It defines how web browsers request web pages from servers and how servers respond. Uses TCP Port 80.
*   **SNMP (Simple Network Management Protocol):** Used by network administrators to monitor and manage network devices like routers, switches, and servers.
*   **Bluetooth:** A short-range wireless technology designed for creating Personal Area Networks (PANs) to connect devices like headphones, keyboards, and smartwatches to a host.
*   **Firewalls:** A network security device that monitors and filters incoming and outgoing network traffic based on a predefined set of security rules. It acts as a barrier between a trusted internal network and an untrusted external network (like the internet).
*   **Directory Services:** A network service that stores, organizes, and provides access to information in a directory. The most famous example is Microsoft's **Active Directory**, which manages all users, computers, and policies on a network.
*   **Network Management:** The broad process of administering, managing, and operating a network, using tools and protocols like SNMP to ensure maximum performance and availability.

---

### **UNIT-VI: Security**

This unit covers the principles and mechanisms for securing data and networks.

*   **Introduction, Security services, Need of Security:** The need for security is framed by the **CIA Triad**:
    *   **Confidentiality:** Ensuring that data is accessible only to authorized users.
    *   **Integrity:** Ensuring that data is not altered or tampered with.
    *   **Availability:** Ensuring that systems and data are available to authorized users when needed.
*   **Key Principles of Security:** The CIA Triad plus:
    *   **Authentication:** Verifying the identity of a user or system.
    *   **Authorization:** Granting a verified user specific permissions to access resources.
    *   **Non-repudiation:** Providing proof that a specific user performed an action, so they cannot deny it later.
*   **Threats and Vulnerabilities, Types of Attacks:**
    *   A **vulnerability** is a weakness in a system. A **threat** is a potential danger that could exploit that weakness. An **attack** is the action of exploiting the vulnerability.
    *   **Types of Attacks:** Eavesdropping (sniffing), Denial of Service (DoS), Man-in-the-Middle, Malware (viruses, worms), Phishing, etc.
*   **ITU-T X.800 Security Architecture for OSI:** A formal model that defines security by outlining three things: security services (what is required), security mechanisms (how to achieve it), and security attacks (what to defend against).
*   **Security Policy and mechanisms:** A **policy** is a high-level document of rules and practices. A **mechanism** is a specific tool (like a firewall or encryption) used to enforce the policy.
*   **Operational Model of Network Security:** A practical approach to security, often described as: **Prevent, Detect, Respond**.
*   **Symmetric and Asymmetric Key Cryptography:**
    *   **Symmetric:** Uses a **single shared key** for both encryption and decryption. It's very fast but has the challenge of securely sharing the key. (e.g., AES).
    *   **Asymmetric:** Uses a **key pair**: a public key for encryption and a private key for decryption. The public key can be shared with anyone. It is slower but solves the key distribution problem. (e.g., RSA).
*   **Security in Network, Transport and Application:**
    *   **IPSec (Network Layer):** Secures communication at the IP packet level, encrypting all data within the packet. It is commonly used to create Virtual Private Networks (VPNs).
    *   **SSL/TLS (Transport Layer):** Secure Sockets Layer (SSL) is the predecessor to Transport Layer Security (TLS). It creates an encrypted channel between two applications (like a browser and a server) to protect the data in transit.
    *   **HTTPS (Application Layer):** This is not a new protocol, but simply HTTP running over an SSL/TLS secured connection.
    *   **S/MIME (Application Layer):** Provides cryptographic security services like digital signatures and encryption for email messages.
*   **Overview of IDS (Intrusion Detection System):** A system that monitors network traffic for suspicious activity and issues alerts when such activity is discovered. It is passive. An **IPS (Intrusion Prevention System)** is an active version that can also take action to block the threat.
