### 10) DNS: Domain Name to IP and Vice Versa

Remembering IP addresses like `172.217.167.78` is difficult for humans. We prefer names like `google.com`. DNS is the service that bridges this gap. When you type a domain name into your browser, your computer performs a DNS lookup to find the corresponding IP address before it can establish a connection.

We will simulate this entire process in Cisco Packet Tracer.

---

#### Step 1: Build the DNS Network Topology

For this simulation, we need a client, a DNS server, and a web server all on the same network.

1.  **Place Devices:**
    - From "End Devices," add one `PC-PT` (our client).
    - Add two `Server-PT` devices. We will configure one as a DNS server and the other as a web server.
    - From "Network Devices" -> "Switches," add one `2960` switch to connect them.

2.  **Name the Devices (Recommended):**
    - Click on the device names to change them. Rename the PC to `Client_PC`, one server to `DNS_Server`, and the other to `Web_Server`. This makes the topology easier to understand.

3.  **Connect the Devices:**
    - Use `Copper Straight-Through` cables to connect `Client_PC`, `DNS_Server`, and `Web_Server` to the switch.

#### Step 2: Configure IP Addresses

All devices need a static IP address to communicate on the network.

1.  **Configure Web_Server:**
    - Click `Web_Server` -> "Desktop" tab -> "IP Configuration."
    - **IP Address:** `192.168.10.100`
    - **Subnet Mask:** `255.255.255.0`

2.  **Configure DNS_Server:**
    - Click `DNS_Server` -> "Desktop" tab -> "IP Configuration."
    - **IP Address:** `192.168.10.200`
    - **Subnet Mask:** `255.255.255.0`

3.  **Configure Client_PC (Crucial Step):**
    - Click `Client_PC` -> "Desktop" tab -> "IP Configuration."
    - **IP Address:** `192.168.10.10`
    - **Subnet Mask:** `255.255.255.0`
    - **DNS Server:** `192.168.10.200` **(This tells the client where to send its DNS queries)**.

#### Step 3: Configure the Server Services

Now we make the servers perform their specific roles.

1.  **Configure the DNS_Server:**
    - Click `DNS_Server` -> "Services" tab -> "DNS."
    - First, make sure the service is turned **On**.
    - In the "Resource Records" section, we will create a record to link a domain name to the `Web_Server`'s IP address.
      - **Name:** `www.example-cpt.com`
      - **Type:** `A Record` (This maps a hostname to an IPv4 address).
      - **Address:** `192.168.10.100` (The IP of our `Web_Server`).
    - Click the **"Add"** button. Your record should now appear in the list.

2.  **Configure the Web_Server:**
    - Click `Web_Server` -> "Services" tab -> "HTTP."
    - Ensure both "HTTP" and "HTTPS" are turned **On**.
    - (Optional) You can click `index.html` and "Edit" to customize the page that will be displayed.

#### Step 4: Test and Verify the DNS Resolution

The configuration is complete. Let's test it from the client's perspective.

**Part A: Domain Name to IP (Web Browser)**

1.  Click `Client_PC` -> "Desktop" tab -> "Web Browser."
2.  In the URL address bar, type the domain name we configured: `www.example-cpt.com` and click "Go."
3.  The default Cisco Packet Tracer web page should appear.

**What just happened?**

- The PC's browser needed to know the IP address for `www.example-cpt.com`.
- It sent a DNS query to its configured DNS server (`192.168.10.200`).
- The DNS server looked in its records, found the entry we created, and sent back a reply: "`www.example-cpt.com` is at `192.168.10.100`".
- The PC's browser then established a direct HTTP connection to `192.168.10.100` and fetched the web page.
- You can watch this entire process step-by-step by switching to **Simulation Mode** and repeating the browser request. Filter for **DNS** and **HTTP** events.

**Part B: Using `nslookup` (Command Line)**

The `nslookup` tool is used specifically for querying the DNS.

1.  Click `Client_PC` -> "Desktop" tab -> "Command Prompt."
2.  **To find the IP for a domain name (Forward Lookup):**

    ```bash
    nslookup www.example-cpt.com
    ```

    The output will correctly show the server that answered the query (`192.168.10.200`) and the IP address it resolved to (`192.168.10.100`).

3.  **To find the domain name for an IP (Reverse Lookup):**
    ````bash
    nslookup 192.168.10.100
    ```    In a real-world scenario with proper PTR (Pointer) records, this would return the domain name. Packet Tracer's basic DNS server doesn't support PTR record configuration in the GUI, so this query will likely time out or fail. However, it correctly demonstrates the command used for a reverse lookup.
    ````

This simulation clearly shows the critical role of DNS in making the network user-friendly and functional.
