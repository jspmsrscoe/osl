### 9) Connect Two Different Networks Using a Router in CPT Simulation

The primary job of a router is to forward traffic between different IP networks. Devices on different networks cannot communicate directly; they need a Layer 3 device to act as an intermediary. This simulation will walk you through the essential steps to connect two separate Local Area Networks (LANs).

**The Goal:** Make a PC on `Network A` successfully `ping` a PC on `Network B`.

---

#### Step 1: Design the IP Addressing Scheme

Before building, you must plan your networks. A clear plan prevents confusion.

- **Network A (Left Side):**
  - Network Address: `192.168.1.0`
  - Subnet Mask: `255.255.255.0`
  - Router Interface IP (Default Gateway): `192.168.1.1`
  - PC IP Address: `192.168.1.10`

- **Network B (Right Side):**
  - Network Address: `192.168.2.0`
  - Subnet Mask: `255.255.255.0`
  - Router Interface IP (Default Gateway): `192.168.2.1`
  - PC IP Address: `192.168.2.10`

Notice that the network addresses (`192.168.1` vs. `192.168.2`) are different, confirming these are two distinct networks.

#### Step 2: Build the Network Topology

1.  **Place Devices:**
    - Add one `1941` Router to the center of the workspace.
    - Add two `2960` Switches, one on the left and one on the right of the router.
    - Add one `PC-PT` next to each switch. Let's call them `PC-A` (left) and `PC-B` (right).

2.  **Connect Devices:**
    - Use the `Copper Straight-Through` cable (solid black line) for all connections.
    - Connect `PC-A` to `Switch-A`.
    - Connect `PC-B` to `Switch-B`.
    - Connect `Switch-A` to the router's `GigabitEthernet0/0` port.
    - Connect `Switch-B` to the router's `GigabitEthernet0/1` port.
    - At this point, all link lights on the connections to the router will be red. This is normal, as router interfaces are turned off by default.

#### Step 3: Configure the PCs

Each PC needs its IP address and, crucially, must know where its "Default Gateway" is. The gateway is the router's address on its local network.

1.  **Configure PC-A:**
    - Click `PC-A` -> "Desktop" tab -> "IP Configuration."
    - **IP Address:** `192.168.1.10`
    - **Subnet Mask:** `255.255.255.0`
    - **Default Gateway:** `192.168.1.1`

2.  **Configure PC-B:**
    - Click `PC-B` -> "Desktop" tab -> "IP Configuration."
    - **IP Address:** `192.168.2.10`
    - **Subnet Mask:** `255.255.255.0`
    - **Default Gateway:** `192.168.2.1`

#### Step 4: Configure the Router

This is the core of the exercise. We will activate and assign an IP address to each of the two router interfaces, placing each one in a different network.

1.  Click the Router, then select the "CLI" (Command Line Interface) tab.
2.  Press `Enter` to get to the prompt. Type `no` for the initial configuration dialog.
3.  Enter the following commands precisely:

    ```bash
    ! Get into privileged mode
    enable

    ! Get into global configuration mode
    configure terminal

    ! --- Configure the interface for Network A (the left side) ---
    interface GigabitEthernet0/0

    ! Assign the IP address and subnet mask from our plan
    ip address 192.168.1.1 255.255.255.0

    ! Turn the interface on. The link light should turn green.
    no shutdown

    ! Exit this interface's configuration
    exit

    ! --- Configure the interface for Network B (the right side) ---
    interface GigabitEthernet0/1

    ! Assign the IP address and subnet mask for the second network
    ip address 192.168.2.1 255.255.255.0

    ! Turn this interface on as well
    no shutdown

    ! Exit the interface configuration
    exit
    ```

#### Step 5: Verify and Test Connectivity

The setup is complete. Now, we must test if it works.

1.  **Open the Command Prompt:** Click on `PC-A`, go to the "Desktop" tab, and open "Command Prompt."

2.  **Ping your own Gateway:** This test ensures `PC-A` can talk to the router.

    ```bash
    ping 192.168.1.1
    ```

    You should get successful replies.

3.  **Ping the other network's Gateway:** This tests if the router is fully configured and operational.

    ```bash
    ping 192.168.2.1
    ```

    This should also be successful.

4.  **Ping the remote PC:** This is the final test of end-to-end communication.
    ```bash
    ping 192.168.2.10
    ```
    The first one or two packets may show "Request timed out" while the network's ARP processes discover the necessary MAC addresses. The following packets should show successful "Reply from 192.168.2.10...".

**Success!** You have successfully enabled communication between two distinct networks.

#### How it Works (Visualizing in Simulation Mode)

If you switch to "Simulation" mode and repeat the final ping (`ping 192.168.2.10`), you can watch the packet's journey:

1.  The packet (PDU) goes from `PC-A` to `Switch-A`.
2.  `Switch-A` knows the destination MAC address is the router's, so it forwards it to the router.
3.  The **Router** receives the frame. It strips off the Layer 2 header (de-encapsulation) and looks at the Layer 3 IP header.
4.  It sees the destination IP is `192.168.2.10`. It checks its routing table and knows that the `192.168.2.0` network is reachable via its `GigabitEthernet0/1` interface.
5.  The router then creates a _new_ Layer 2 frame, puts the packet inside (re-encapsulation), and sends it out the `GigabitEthernet0/1` port to `Switch-B`.
6.  `Switch-B` forwards the frame to `PC-B`. The ping is successful.
