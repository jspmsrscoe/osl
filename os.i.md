### 5) OSI Layer Simulation in Cisco Packet Tracer

The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstract layers. Packet Tracer's simulation mode allows you to see how data is encapsulated with headers and trailers as it moves down the OSI model at the source device and de-encapsulated as it moves up the model at the destination.

We will simulate a client requesting a web page from a server.

---

#### Step 1: Build the Topology

1.  **Add End Devices:**
    - From the "End Devices" menu, drag one `PC-PT` (the client) and one `Server-PT` (the server) into the workspace.
2.  **Add a Switching Device:**
    - From "Network Devices" -> "Switches," drag a `2960` switch and place it between the PC and the server.
3.  **Connect the Devices:**
    - Using a `Copper Straight-Through` cable from the "Connections" menu, connect the PC's `FastEthernet0` port to the switch's `FastEthernet0/1` port.
    - Connect the server's `FastEthernet0` port to the switch's `FastEthernet0/2` port.

#### Step 2: Configure IP Addresses and Server Services

1.  **Configure the PC:**
    - Click on the PC, go to the "Desktop" tab -> "IP Configuration."
    - Set the IP Address to `192.168.1.10`.
    - Set the Subnet Mask to `255.255.255.0`.
2.  **Configure the Server:**
    - Click on the server, go to the "Desktop" tab -> "IP Configuration."
    - Set the IP Address to `192.168.1.100`.
    - Set the Subnet Mask to `255.255.255.0`.
    - Now, go to the "Services" tab. Ensure the "HTTP" service is turned **On**. This makes the server function as a web server.

#### Step 3: Prepare and Run the Simulation

1.  **Switch to Simulation Mode:**
    - In the bottom-right corner of the Packet Tracer window, toggle from "Realtime" to "Simulation." This will open the Simulation Panel.
2.  **Edit Filters:**
    - The simulation can show many protocols, which can be overwhelming. Click "Edit Filters" in the Simulation Panel.
    - Uncheck the "Show All/None" box to clear everything, and then check only **HTTP**. Packet Tracer will automatically include the lower-level protocols that HTTP depends on (like TCP and IP).
3.  **Initiate the Traffic:**
    - Click on the client PC.
    - Go to the "Desktop" tab and open the "Web Browser."
    - In the URL bar, type the IP address of the server: `192.168.1.100` and click "Go."

#### Step 4: Analyze the Packet (PDU) Details

Instead of data moving, you will now see a small, colored envelope (a PDU, or Protocol Data Unit) appear on your PC, and an event will be listed in the Simulation Panel. This is your HTTP request, paused in time.

1.  **Inspect the Packet at the Source (Encapsulation):**
    - In the Simulation Panel's "Event List," click on the colored square for the first HTTP event.
    - A window titled "PDU Information" will open. This is where you can see the OSI model in action.
    - Click the **"OSI Model"** tab. You will see the data being processed **down** the layers of the client PC.

    - **Layer 7 (Application):** The data starts here. You can see the message: "The HTTP client sends an HTTP request to the server."
    - **Layer 4 (Transport):** The data is encapsulated in a TCP segment. Notice the Source Port (a random number above 1023) and the Destination Port (**80**, the standard for HTTP).
    - **Layer 3 (Network):** The segment is encapsulated in an IP packet. Notice the Source IP (`192.168.1.10`) and Destination IP (`192.168.1.100`).
    - **Layer 2 (Data Link):** The packet is encapsulated in an Ethernet frame. Notice the Source MAC address (of the PC) and the Destination MAC address (of the server). _Note: An ARP process might run first to find this MAC address._
    - **Layer 1 (Physical):** The frame is ready to be sent out as a stream of bits onto the network cable.

2.  **Follow the Packet to the Destination (De-encapsulation):**
    - Close the PDU Information window.
    - Click the **"Capture / Forward"** button (the right-pointing arrow) in the Simulation Panel.
    - The packet will move from the PC to the switch. Click the packet at the switch. The PDU Information window will show that the switch only processes up to **Layer 2**. It reads the destination MAC address to decide which port to forward the frame to.
    - Click "Capture / Forward" again. The packet moves from the switch to the server.
    - Now, click the envelope at the server. In the "OSI Model" tab, you'll see the process in reverse (**de-encapsulation**).

    - **Layer 1 (Physical):** The server receives the bits from the cable.
    - **Layer 2 (Data Link):** The Ethernet frame is processed. The server confirms the destination MAC address matches its own. The frame header is stripped away.
    - **Layer 3 (Network):** The IP packet is processed. The server confirms the destination IP is its own. The IP header is stripped away.
    - **Layer 4 (Transport):** The TCP segment is processed. The server checks the destination port (80) to know which application (the web server) should receive the data. The TCP header is stripped away.
    - **Layer 7 (Application):** The raw data (the HTTP GET request) is delivered to the HTTP server daemon.

By clicking "Capture / Forward" repeatedly, you can watch the server's HTTP reply get encapsulated, travel back across the network, and be de-encapsulated by the client PC, resulting in the web page loading in the browser.
