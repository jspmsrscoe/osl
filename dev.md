### 2) Working Simulation of Networking Devices in Cisco Packet Tracer

Cisco Packet Tracer allows you to build virtual networks and observe how data travels through them. A key part of this is understanding the role of different networking devices. Here’s how to simulate the basic functions of hubs, switches, routers, and repeaters.

---

#### A) Hub Simulation (Layer 1 Device)

A hub is a basic networking device that operates at the Physical Layer (Layer 1) of the OSI model. It is not "intelligent." When it receives a data packet on one port, it simply broadcasts that packet to every other port.

**Simulation Steps:**

1.  **Build the Topology:**
    - Open Cisco Packet Tracer.
    - From the bottom-left menu, select "Network Devices" -> "Hubs." Drag and drop a `Hub-PT` into the workspace.
    - Select "End Devices" and drag three or four `PC-PT` devices into the workspace.
    - Connect each PC to the hub. Select "Connections" (the lightning bolt icon), choose the `Copper Straight-Through` cable (solid black line), click on a PC, select `FastEthernet0`, then click on the hub and select a `Port`. Repeat for all PCs.

2.  **Configure IP Addresses:**
    - Click on the first PC, go to the "Desktop" tab, and click "IP Configuration."
    - Set a static IP address, for example, `192.168.1.1` with a subnet mask of `255.255.255.0`.
    - Do this for all other PCs, giving each a unique IP address within the same network (e.g., `192.168.1.2`, `192.168.1.3`, etc.).

3.  **Run the Simulation:**
    - Switch from "Realtime" to "Simulation" mode using the toggle in the bottom-right corner.
    - In the simulation panel, click "Edit Filters" and ensure that only "ICMP" is selected.
    - Select the "Add Simple PDU" tool (the closed envelope icon) from the right-side toolbar.
    - Click on your source PC (e.g., PC0 at 192.168.1.1) and then on your destination PC (e.g., PC2 at 192.168.1.3). An ICMP packet will appear on the source PC.
    - Click the "Capture / Forward" button (the arrow pointing to the right) to see the packet move step-by-step.

**What to Observe:**
The packet will travel from the source PC to the hub. The hub will then duplicate the packet and send it to **all** connected PCs, except for the one it came from. The PCs that are not the intended destination will drop the packet (indicated by a red 'X'), while the correct destination PC will accept it and send a reply. This demonstrates the broadcast nature of a hub.

---

#### B) Switch Simulation (Layer 2 Device)

A switch is a more intelligent device that operates at the Data Link Layer (Layer 2). It learns the MAC (Media Access Control) addresses of devices connected to its ports and forwards packets only to the intended recipient, reducing unnecessary network traffic.

**Simulation Steps:**

1.  **Build the Topology:**
    - Create a new workspace.
    - Select "Network Devices" -> "Switches" and drag a `2960` switch into the workspace.
    - Add three or four PCs and connect them to the switch using `Copper Straight-Through` cables.

2.  **Configure IP Addresses:**
    - Assign unique IP addresses to each PC within the same subnet, just as you did for the hub simulation (e.g., `192.168.1.1`, `192.168.1.2`, etc.).

3.  **Run the Simulation:**
    - Switch to "Simulation" mode. Edit filters and select "ARP" and "ICMP".
    - Use the "Add Simple PDU" tool to create a packet from a source PC to a destination PC.
    - Click "Capture / Forward."

**What to Observe:**

- **First Packet (ARP):** The first time a PC communicates, the switch doesn't know which port the destination PC is on. The source PC will send an **ARP (Address Resolution Protocol)** request to find the MAC address of the destination IP. The switch will broadcast this ARP request to all ports. The destination PC will reply, and the switch will record the MAC addresses and corresponding ports in its MAC Address Table.
- **Subsequent Packets (ICMP):** Now that the switch has learned the addresses, when the source PC sends the actual ICMP (ping) packet, the switch will look up the destination MAC address in its table and forward the packet **only** to the correct port. You will see a direct, unicast communication path.

You can inspect the switch's MAC table by clicking on the switch, going to the "CLI" tab, and typing `show mac-address-table`.

---

#### C) Router Simulation (Layer 3 Device)

A router is a Layer 3 device used to connect **different networks**. It uses IP addresses to route traffic between these networks.

**Simulation Steps:**

1.  **Build the Topology (Two Networks):**
    - Select "Network Devices" -> "Routers" and add a `1941` router.
    - Add two `2960` switches.
    - Add two PCs for each switch.
    - Connect the two PCs to Switch0. Connect the other two PCs to Switch1.
    - Connect Switch0 to the router's `GigabitEthernet0/0` port.
    - Connect Switch1 to the router's `GigabitEthernet0/1` port.

2.  **Configure IP Addresses (Crucial Step):**
    - **Network 1 (left side):**
      - PC0: IP `192.168.1.10`, Mask `255.255.255.0`, **Default Gateway `192.168.1.1`**
      - PC1: IP `192.168.1.11`, Mask `255.255.255.0`, **Default Gateway `192.168.1.1`**
    - **Network 2 (right side):**
      - PC2: IP `192.168.2.10`, Mask `255.255.255.0`, **Default Gateway `192.168.2.1`**
      - PC3: IP `192.168.2.11`, Mask `255.255.255.0`, **Default Gateway `192.168.2.1`**

3.  **Configure the Router:**
    - Click the router, go to the "CLI" (Command Line Interface) tab.
    - Enter the following commands:

      ```bash
      enable
      configure terminal

      ! Configure the interface for the first network
      interface GigabitEthernet0/0
      ip address 192.168.1.1 255.255.255.0
      no shutdown

      ! Configure the interface for the second network
      interface GigabitEthernet0/1
      ip address 192.168.2.1 255.255.255.0
      no shutdown

      exit
      ```

    - The `no shutdown` command activates the interface.

4.  **Run the Simulation:**
    - Switch to "Simulation" mode.
    - Use the "Add Simple PDU" tool to send a packet from a PC in Network 1 (e.g., PC0) to a PC in Network 2 (e.g., PC2).
    - Click "Capture / Forward."

**What to Observe:**
The packet will go from PC0 to Switch0. Since the destination is on a different network, Switch0 will forward the packet to its default gateway (the router). The router will receive the packet, look at the destination IP (`192.168.2.10`), check its routing table, and determine that this network is reachable via its `GigabitEthernet0/1` interface. It will then forward the packet to Switch1, which finally delivers it to PC2. This demonstrates inter-network communication.

---

#### D) Repeater Simulation (Layer 1 Device)

A repeater is a Layer 1 device used to regenerate and re-amplify a signal, allowing it to travel a longer distance. In Packet Tracer, it functions like a two-port hub.

**Simulation Steps:**

1.  **Build the Topology:**
    - Go to "Network Devices" -> "Hubs" and select the `Repeater-PT`.
    - Add two PCs.
    - Connect one PC to `Port0` of the repeater and the other PC to `Port1` using `Copper Straight-Through` cables.

2.  **Configure IPs:**
    - Assign IP addresses from the same subnet to both PCs (e.g., `192.168.1.1` and `192.168.1.2`).

3.  **Run the Simulation:**
    - Switch to "Simulation" mode and send a simple PDU from one PC to the other.
    - Click "Capture / Forward."

**What to Observe:**
The repeater will receive the signal on one port and simply regenerate and forward it out the other port. It performs no filtering or addressing logic. Its purpose is purely to extend the physical range of a network segment.
