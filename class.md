### 8) Classful Addressing using CPT Simulation

Classful addressing was the original method of categorizing IPv4 addresses. It divides the entire address space into five classes (A, B, C, D, E), with A, B, and C being used for network hosts. Each class has a fixed, non-negotiable subnet mask, which defines how many bits are used for the network portion and how many are for the host portion.

- **Class A:**
  - **Range:** `1.0.0.0` to `126.255.255.255`
  - **Default Subnet Mask:** `255.0.0.0`
  - **Structure:** `NETWORK.HOST.HOST.HOST`
  - **Designed for:** A few massive networks with millions of hosts each.

- **Class B:**
  - **Range:** `128.0.0.0` to `191.255.255.255`
  - **Default Subnet Mask:** `255.255.0.0`
  - **Structure:** `NETWORK.NETWORK.HOST.HOST`
  - **Designed for:** A moderate number of medium-to-large sized networks.

- **Class C:**
  - **Range:** `192.0.0.0` to `223.255.255.255`
  - **Default Subnet Mask:** `255.255.255.0`
  - **Structure:** `NETWORK.NETWORK.NETWORK.HOST`
  - **Designed for:** A large number of small networks, each with a maximum of 254 hosts.

**The Goal of This Simulation:** To build three separate networks, one for each class (A, B, and C), and use a router to enable communication between them. This demonstrates how routers are essential for connecting distinct network address spaces.

---

#### Step 1: Build the Topology

1.  **Add a Router:** From "Network Devices" -> "Routers," drag a `1941` router to the center of the workspace.
2.  **Add Switches:** From "Network Devices" -> "Switches," drag three `2960` switches and place them around the router.
3.  **Add End Devices:** From "End Devices," drag a `PC-PT` next to each switch. Let's name them `PC_A`, `PC_B`, and `PC_C` for clarity.
4.  **Connect Devices:**
    - Use `Copper Straight-Through` cables for all connections.
    - Connect `PC_A` to `Switch_A`.
    - Connect `PC_B` to `Switch_B`.
    - Connect `PC_C` to `Switch_C`.
    - Connect `Switch_A` to the router's `GigabitEthernet0/0` port.
    - Connect `Switch_B` to the router's `GigabitEthernet0/1` port.
    - Connect `Switch_C` to the router's `GigabitEthernet0/2` port.

Your topology should look like a central router with three branches, each containing a switch and a PC.

#### Step 2: Configure IP Addresses on the PCs

This is the most critical step for demonstrating the classes.

1.  **Configure PC_A (Class A Network):**
    - Click `PC_A` -> "Desktop" tab -> "IP Configuration."
    - IP Address: `10.0.0.10`
    - Subnet Mask: `255.0.0.0` (This is the default mask for Class A).
    - Default Gateway: `10.0.0.1` (This will be the router's IP address on this network).

2.  **Configure PC_B (Class B Network):**
    - Click `PC_B` -> "Desktop" tab -> "IP Configuration."
    - IP Address: `172.16.0.10`
    - Subnet Mask: `255.255.0.0` (The default mask for Class B).
    - Default Gateway: `172.16.0.1`

3.  **Configure PC_C (Class C Network):**
    - Click `PC_C` -> "Desktop" tab -> "IP Configuration."
    - IP Address: `192.168.1.10`
    - Subnet Mask: `255.255.255.0` (The default mask for Class C).
    - Default Gateway: `192.168.1.1`

#### Step 3: Configure the Router

The router needs an IP address on each of the three different networks to act as the gateway. We will configure this using the Command Line Interface (CLI).

1.  Click the Router, then go to the "CLI" tab.
2.  You will see a prompt asking `Would you like to enter the initial configuration dialog? [yes/no]:`. Type `no` and press Enter.
3.  Enter the following commands one by one:

    ```bash
    ! Enter privileged EXEC mode
    enable

    ! Enter global configuration mode
    configure terminal

    ! --- Configure the interface for the Class A network ---
    interface GigabitEthernet0/0
    ! Assign the IP address and the correct classful subnet mask
    ip address 10.0.0.1 255.0.0.0
    ! Add a description for clarity
    description Link to Class A Network
    ! Activate the interface
    no shutdown
    exit

    ! --- Configure the interface for the Class B network ---
    interface GigabitEthernet0/1
    ip address 172.16.0.1 255.255.0.0
    description Link to Class B Network
    no shutdown
    exit

    ! --- Configure the interface for the Class C network ---
    interface GigabitEthernet0/2
    ip address 192.168.1.1 255.255.255.0
    description Link to Class C Network
    no shutdown
    exit
    ```

4.  After issuing the `no shutdown` commands, you will see the link lights on the connections turn from red to green, indicating the interfaces are active.

#### Step 4: Verify and Test Connectivity

Now we will use the `ping` command to verify that our configuration works.

1.  **Test Intra-Network Communication:**
    - Open the Command Prompt on `PC_A`.
    - Ping its own default gateway: `ping 10.0.0.1`
    - The ping should be successful. This confirms that `PC_A` can communicate with its local router interface.

2.  **Test Inter-Network Communication (The Goal!):**
    - From the Command Prompt on `PC_A`, ping the PC in the Class C network.
    - Type: `ping 192.168.1.10`
    - The first packet might time out while the ARP protocol works to resolve MAC addresses, but the subsequent packets should succeed. You will see "Reply from 192.168.1.10...".

3.  **Trace the Path:**
    - From `PC_A`'s Command Prompt, trace the route to `PC_B`.
    - Type: `tracert 172.16.0.10`
    - The output will show two hops:
      1.  `10.0.0.1` (Your default gateway)
      2.  `172.16.0.10` (The final destination)

**What This Simulation Shows:**

- Each PC is in a completely separate network, defined by its classful IP address and default subnet mask.
- `PC_A` cannot talk directly to `PC_B` because their network IDs (`10` and `172.16`) are different.
- When `PC_A` wants to send a packet to `PC_B`, it recognizes the destination is outside its local network. It therefore sends the packet to its **default gateway**.
- The router receives the packet, inspects the destination IP (`172.16.0.10`), looks at its routing table, and knows that this network is connected to its `GigabitEthernet0/1` interface. It then forwards the packet to `PC_B`.
- This successfully demonstrates the fundamental role of a router in connecting different IP networks, whether they are classful or classless.
