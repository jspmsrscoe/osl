---

### **The OSI Model (7 Layers)**

A conceptual framework used to understand and standardize network functions.

*   **Layer 7: Application**
    *   **Feature:** The user interface to the network. Provides protocols (HTTP, DNS, FTP) that user-facing applications use directly.
    *   **Analogy:** The app on your phone.

*   **Layer 6: Presentation**
    *   **Feature:** The data translator. Handles data formatting, encryption/decryption, and compression to ensure data is readable by the application layer.
    *   **Analogy:** A universal translator for different languages.

*   **Layer 5: Session**
    *   **Feature:** The dialogue controller. Establishes, manages, and terminates communication sessions (conversations) between two applications.
    *   **Analogy:** A meeting moderator who starts and stops the conversation.

*   **Layer 4: Transport**
    *   **Feature:** End-to-end reliability and process communication. Uses TCP (reliable) or UDP (unreliable) and **port numbers** to manage data flow and error control between applications.
    *   **Analogy:** A post office sorting mail for a specific department (process) within a large building (computer).

*   **Layer 3: Network**
    *   **Feature:** Packet routing and logical addressing. Uses **IP addresses** to route packets across multiple networks and find the best path from source to destination.
    *   **Analogy:** The GPS system that finds the best route for a delivery truck.

*   **Layer 2: Data Link**
    *   **Feature:** Hop-to-hop delivery on a local network. Uses **MAC addresses** to transfer data frames between devices on the same physical network and performs error detection.
    *   **Analogy:** The local mail carrier delivering a letter to a specific street address on their route.

*   **Layer 1: Physical**
    *   **Feature:** Transmitting raw bits. Defines the physical hardware, such as cables, connectors, and electrical signals, for sending 0s and 1s over the medium.
    *   **Analogy:** The physical road the delivery truck drives on.

---

### **The TCP/IP Model (4 or 5 Layers)**

A practical model that the modern internet is based on. It's more condensed than the OSI model.

*   **Application Layer**
    *   **Feature:** Combines the functions of OSI layers 5, 6, and 7. It handles user-facing protocols (HTTP, DNS), data representation, and session management.

*   **Transport Layer**
    *   **Feature:** Identical to the OSI Transport Layer. It provides process-to-process communication using TCP or UDP and port numbers.

*   **Internet Layer** (or Network Layer)
    *   **Feature:** Identical to the OSI Network Layer. It uses the Internet Protocol (IP) for logical addressing and routing packets across networks.

*   **Network Access Layer** (or Link Layer)
    *   **Feature:** Combines the functions of OSI layers 1 and 2. It handles everything related to the physical transmission of data, including MAC addresses, frames, and the physical hardware.
---

### **UNIT-I: Introduction and Data Communication Components**

This unit sets the foundation for everything that follows. It's about what a network is, its basic building blocks, and the models we use to understand it.

*   **Computer Networks and Distributed Systems:** A **Computer Network** is a collection of interconnected computers that can share resources and data. A **Distributed System** is a type of system where components are located on different networked computers, which communicate and coordinate their actions to appear as a single coherent system to the end-user (e.g., the World Wide Web).
*   **Classifications of Computer Networks:** Networks are classified by their size and geographical scope:
    *   **LAN (Local Area Network):** Covers a small area like a single building or campus.
    *   **MAN (Metropolitan Area Network):** Covers a city.
    *   **WAN (Wide Area Network):** Covers a large geographical area, like a country or the entire globe (the internet is the largest WAN).
*   **Preliminaries of Layered Network Structures:** Complex systems like networks are broken down into layers to make them easier to manage and design. Each layer provides a service to the layer above it and uses the services of the layer below it. This is the core principle behind the OSI and TCP/IP models.
*   **Representation of Data and Its Flow:** Data flows through a network as a stream of **bits** (0s and 1s). This flow can be:
    *   **Simplex:** Communication is one-way only (e.g., a radio broadcast).
    *   **Half-Duplex:** Communication can be two-way, but not at the same time (e.g., a walkie-talkie).
    *   **Full-Duplex:** Communication is two-way simultaneously (e.g., a telephone call).
*   **Various Connection Topology:** The physical or logical arrangement of a network.
    *   **Bus:** All devices share a single main cable.
    *   **Star:** All devices connect to a central hub or switch (most common in modern LANs).
    *   **Ring:** Each device is connected to exactly two other devices, forming a circle.
    *   **Mesh:** Devices are interconnected, providing multiple paths for data (highly redundant).
    *   **Hybrid:** A combination of two or more topologies.
*   **Protocols and Standards:** A **protocol** is a set of rules that governs communication (like a language). **Standards** (e.g., IEEE, IETF) are agreed-upon specifications that ensure equipment from different manufacturers can work together.
*   **OSI Model:** A 7-layer conceptual model that standardizes the functions of a network. (Application, Presentation, Session, Transport, Network, Data Link, Physical).
*   **TCP/IP Model:** A 4 or 5-layer practical model that the internet is based on. (Application, Transport, Internet/Network, Data Link, Physical).
*   **Transmission Media:** The physical path through which data travels.
    *   **Wired:** Twisted-Pair Copper Cable, Coaxial Cable, Fiber Optic Cable.
    *   **Wireless:** Radio waves (Wi-Fi, Bluetooth), Microwaves.
*   **Network Architectures:**
    *   **Client-Server:** A central, powerful server provides services to many less-powerful clients (e.g., a web server and your browser).
    *   **Peer-To-Peer (P2P):** All devices have equal capabilities and can act as both a client and a server (e.g., BitTorrent).
    *   **Hybrid:** Combines elements of both, like a P2P application that uses a central server for coordination.
*   **Network Devices:**
    *   **Bridge/Switch:** A Layer 2 device that connects network segments and uses MAC addresses to filter and forward traffic.
    *   **Router:** A Layer 3 device that connects different networks and uses IP addresses to route traffic between them.
    *   **Gateway:** A device that connects two networks that use different protocols (often used to refer to a router connecting a LAN to the internet).
    *   **Access Point:** A device that allows wireless devices to connect to a wired network.
*   **Line Coding Schemes:** Methods for converting digital data (0s and 1s) into a digital signal for transmission.
    *   **Manchester Encoding:** A `0` is represented by a high-to-low voltage transition, and a `1` by a low-to-high transition. This guarantees a transition in the middle of each bit, which helps with clock synchronization.
    *   **Differential Manchester Encoding:** A transition always occurs in the middle of the bit for synchronization. A `1` is represented by *no* transition at the beginning of the bit interval, and a `0` is represented by a transition.
*   **Spread Spectrum:** A technique used to make a signal resistant to interference and eavesdropping by spreading it over a wider frequency band.
    *   **FHSS (Frequency Hopping):** The signal rapidly hops between different frequencies in a pseudo-random but predictable sequence.
    *   **DSSS (Direct Sequence):** Spreads the signal by multiplying it with a "chipping code," a high-frequency signal.

---

### **UNIT-II: Data Link Layer**

This layer is responsible for **node-to-node** or **hop-to-hop** delivery of data. It takes packets from the Network Layer and encapsulates them into **frames** for transmission. It deals with MAC addresses, physical access to the media, and error detection.

*   **Wired LAN, Wireless LAN and Virtual LAN:**
    *   **Wired LAN:** A LAN that uses physical cables (e.g., Ethernet).
    *   **Wireless LAN (WLAN):** A LAN that uses radio waves (e.g., Wi-Fi).
    *   **Virtual LAN (VLAN):** A logical grouping of devices on a network, regardless of their physical location. VLANs allow you to segment a single physical switch into multiple virtual switches for security and traffic management.
*   **Multiplexing:** A technique to send multiple signals over a single medium.
    *   **Frequency Division (FDM):** Divides the channel's frequency band into smaller sub-channels, one for each signal.
    *   **Time Division (TDM):** Gives each signal a specific time slot in which to transmit.
    *   **Wave Division (WDM):** Used in fiber optics; sends multiple signals using different wavelengths (colors) of light.
*   **Error Detection and Error Correction:**
    *   **Error Detection:** Identifies that an error has occurred (e.g., CRC).
    *   **Error Correction:** Can identify and fix the error without re-transmission (e.g., Hamming Code).
*   **Block coding, Hamming Distance, CRC:**
    *   **Block coding:** Adds redundant bits to a block of data to help detect/correct errors.
    *   **Hamming Distance:** The number of bit positions in which two codewords differ. A higher Hamming distance means better error detection capabilities.
    *   **CRC (Cyclic Redundancy Check):** A powerful error-detection algorithm that uses polynomial division to generate a checksum.
*   **Flow Control and Error Control Protocols:**
    *   **Flow Control:** Manages the data rate to ensure a fast sender doesn't overwhelm a slow receiver.
    *   **Error Control:** Manages lost or corrupted frames, usually through acknowledgments (ACKs) and retransmissions.
*   **Stop and Wait:** The simplest protocol. The sender sends one frame and then waits for an ACK before sending the next one. Very inefficient.
*   **Go-Back–N ARQ & Selective Repeat ARQ (Sliding Window Protocols):**
    *   **Sliding Window:** Allows the sender to transmit multiple frames (a "window") before waiting for an ACK, improving efficiency.
    *   **Go-Back-N:** If a frame is lost, the sender re-transmits that frame and all subsequent frames in the window.
    *   **Selective Repeat:** If a frame is lost, the sender only re-transmits the specific frame that was lost. The receiver can buffer out-of-order frames. More efficient but more complex.
*   **Piggybacking:** A technique to improve efficiency where an acknowledgment for a received frame is sent along with (piggybacked onto) an outgoing data frame.
*   **Random Access / Multiple Access Protocols:** Rules for sharing a common communication medium.
    *   **ALOHA (Pure and Slotted):** Early, simple protocols. In Pure ALOHA, stations transmit whenever they want, leading to many collisions. Slotted ALOHA synchronizes transmissions into time slots to reduce collisions.
    *   **CSMA/CD (Carrier Sense Multiple Access with Collision Detection):** Used in classic Ethernet. "Listen before you talk." If a collision is detected, stations back off for a random time before trying again.
    *   **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance):** Used in Wi-Fi. Tries to *avoid* collisions before they happen, often by using a "Request to Send/Clear to Send" (RTS/CTS) mechanism.
*   **Ethernet:** The dominant wired LAN technology. It defines the standards for cabling, signaling, and the CSMA/CD access method.

---

### **UNIT-III: Network Layer**

This layer is responsible for **host-to-host** or **end-to-end** delivery of data. It handles the logical addressing and routing of **packets** across multiple networks.

*   **Function of Network layer:** Logical addressing (IP addresses) and routing (determining the best path for a packet to take from source to destination).
*   **Switching Techniques:** How data is moved through a network.
    *   **Circuit Switching:** A dedicated physical path is established between sender and receiver for the entire duration of the communication (e.g., a traditional phone call).
    *   **Packet Switching:** Data is broken into small packets, each of which is routed independently through the network. The internet is a packet-switched network.
*   **IP Protocol:** The core protocol of the Network Layer. It is an **unreliable** and **connectionless** protocol responsible for addressing and routing packets.
*   **Logical Addressing – IPV4, IPV6:**
    *   **IPv4:** The legacy 32-bit addressing scheme (e.g., `192.168.1.1`). It is running out of addresses.
    *   **IPv6:** The new 128-bit addressing scheme (e.g., `2001:0db8:85a3::8a2e:0370:7334`). Provides a vastly larger address space.
*   **Subnet:** The process of dividing a large network into smaller, more manageable sub-networks.
*   **CIDR (Classless Inter-Domain Routing):** The modern method of allocating IP addresses and routing. It replaces the old classful system (A, B, C) and allows for variable-length subnet masks, which is much more efficient.
*   **Address Mapping:** Protocols that map addresses from one layer to another.
    *   **ARP (Address Resolution Protocol):** Maps a known IP address to an unknown MAC address. (Query: "Who has IP address 192.168.1.10? Tell me your MAC address.")
    *   **RARP (Reverse ARP):** An obsolete protocol that mapped a known MAC address to an IP address.
    *   **BOOTP and DHCP:** BOOTP is an older protocol for diskless workstations to get an IP address. **DHCP (Dynamic Host Configuration Protocol)** is its modern successor. DHCP is a client-server protocol that automatically provides a host with its IP address, subnet mask, default gateway, and DNS server information.
*   **Delivery, Forwarding and Unicast Routing Protocols:**
    *   **Delivery:** Getting a packet to its destination.
    *   **Forwarding:** The action a router takes when it receives a packet: it looks up the destination IP in its routing table and forwards the packet out the correct interface.
    *   **Unicast Routing Protocols:** The protocols that routers use to build and maintain their routing tables. They exchange information with other routers to learn about the network's topology. Examples include **RIP**, **OSPF**, and **BGP**.
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
