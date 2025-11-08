### 4) Networking Commands

These commands are fundamental tools for network testing, verification, and troubleshooting. We'll explore them in the Cisco Packet Tracer (CPT) simulation environment and on a Fedora (Linux) system.

---

#### Part A: Commands in Cisco Packet Tracer

In CPT, you run these commands from the command prompt of a virtual end device, like a PC or a laptop.

**How to Access the Command Prompt in CPT:**

1.  Click on a PC in your topology.
2.  Go to the "Desktop" tab.
3.  Click the "Command Prompt" icon.

---

##### **1. `ipconfig` and `ipconfig /all`**

This command is used to display the current TCP/IP network configuration values.

- **`ipconfig`**: Shows the basic information for each network adapter: IP Address, Subnet Mask, and Default Gateway.
- **`ipconfig /all`**: Provides a more detailed report, including the MAC Address (listed as Physical Address), DNS Server information, and more.

**Simulation Steps:**

1.  **Build a simple network:** Place a PC, a switch, and a router. Connect the PC to the switch and the switch to the router.
2.  **Configure the PC:** Assign a static IP address to the PC (e.g., `192.168.1.10`), a subnet mask (`255.255.255.0`), and a default gateway (the router's IP, e.g., `192.168.1.1`).
3.  **Open the PC's Command Prompt.**
4.  **Run the commands:**
    - Type `ipconfig` and press Enter. You will see the basic IP info you just configured.
    - Type `ipconfig /all` and press Enter. You will see the same IP info plus the PC's unique MAC address.

**What to Observe:**
This command verifies that the IP settings on a device are correct. It's the very first thing you should check when a device can't connect to the network.

---

##### **2. `ping`**

The `ping` command tests reachability. It sends a special message called an ICMP "Echo Request" to a target IP address and waits for an "Echo Reply." It's the primary tool for checking if a device is online and accessible.

**Simulation Steps:**

1.  **Build a two-network topology:** Use the router topology from tutorial #2, where you have two separate networks (e.g., `192.168.1.0/24` and `192.168.2.0/24`) connected by a router.
2.  **Open the Command Prompt on a PC in the first network** (e.g., PC0 with IP `192.168.1.10`).
3.  **Ping a device on the same network:**
    - Type `ping 192.168.1.11` (the IP of another PC in the same network) and press Enter.
    - You should see "Reply from..." messages, indicating success. The first ping might time out while ARP resolves the MAC address; this is normal.
4.  **Ping the default gateway:**
    - Type `ping 192.168.1.1` (the router's interface IP for this network).
    - Successful replies confirm you can reach your gateway.
5.  **Ping a device on the other network:**
    - Type `ping 192.168.2.10` (the IP of a PC on the second network).
    - If your router is configured correctly, you will get successful replies. This confirms you have end-to-end connectivity across different networks.

**What to Observe:**

- **"Reply from..."**: The connection is good.
- **"Request timed out"**: The command received no reply. This could mean the destination device is offline, a firewall is blocking the ping, or there's a routing problem along the way.
- **"Destination host unreachable"**: Your own device or a router along the path doesn't know how to get to the destination network.

---

##### **3. `tracert`**

The `tracert` (Trace Route) command shows the path that a packet takes to reach a destination. It lists all the routers (or "hops") the packet passes through. This is extremely useful for diagnosing where a connection is failing in a larger network.

**Simulation Steps:**

1.  **Use the same two-network topology as the `ping` example.** For a better demonstration, you could add a second router to create more "hops."
2.  **Open the Command Prompt on a PC** in the first network (e.g., PC0 at `192.168.1.10`).
3.  **Trace the route to a PC on the other network:**
    - Type `tracert 192.168.2.10` and press Enter.

**What to Observe:**
The output will list the hops, line by line:

1.  The first hop will be your default gateway (the first router, `192.168.1.1`).
2.  The final hop will be the destination PC itself (`192.168.2.10`).

If there were more routers in between, each one would be listed in order. If the trace fails, it will show you the last successful hop, giving you a clue as to where the network problem lies.

---

#### Part B: Commands in Fedora (Linux)

In Fedora, you run these commands from the Terminal.

---

##### **1. `ip address` (The `ipconfig` Equivalent)**

The `ipconfig` command is specific to Windows. The modern Linux equivalent is the `ip` command. The older, deprecated command is `ifconfig`.

- **Command:** `ip address` or its shorter version, `ip a`.

**How to Use:**

1.  Open a Terminal in Fedora.
2.  Type `ip a` and press Enter.

**What to Observe:**
You'll see a list of your network interfaces (e.g., `lo` for loopback, `enp0s3` or `wlan0` for your Ethernet or Wi-Fi card). For your active connection, you will find:

- `inet`: Your IPv4 address, followed by the subnet mask in CIDR notation (e.g., `/24`).
- `ether`: Your MAC address.

---

##### **2. `ping`**

The `ping` command in Linux works just like in CPT but with one key difference: **it does not stop automatically**. It will continue sending packets until you manually stop it with `Ctrl + C`.

**How to Use:**

1.  Open the Terminal.
2.  To ping Google's DNS server 4 times:
    ```bash
    ping -c 4 8.8.8.8
    ```
    _(The `-c 4` flag tells it to send only 4 packets.)_
3.  To ping a domain name (which also tests DNS):
    ```bash
    ping google.com
    ```
    _(Remember to press `Ctrl + C` to stop it.)_

---

##### **3. `nslookup`**

The `nslookup` (Name Server Lookup) command is used to query the Domain Name System (DNS) to find the IP address associated with a domain name, or vice versa.

**How to Use:**

1.  Open the Terminal.
2.  To find the IP address for google.com:
    ```bash
    nslookup google.com
    ```
3.  To find the domain name for an IP address (a reverse lookup):
    ```bash
    nslookup 8.8.8.8
    ```

**What to Observe:**
The output will show you which DNS server was used to answer your query and then provide the "Non-authoritative answer," which lists the corresponding IP address(es) or domain name. This is a great tool for troubleshooting DNS issues.
