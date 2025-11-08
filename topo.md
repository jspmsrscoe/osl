### 3) Working Simulation of Networking Topologies in Cisco Packet Tracer

Network topology refers to the arrangement of the elements (links, nodes, etc.) of a communication network. Cisco Packet Tracer is an ideal tool for visualizing how these different arrangements affect data flow.

---

#### A) Star Topology Simulation

In a star topology, all devices are connected to a central device, like a hub or a switch. It's the most common topology in modern LANs.

**Simulation Steps:**

1.  **Build the Topology:**
    - From the "Network Devices" menu, select "Switches" and drag a `2960` switch into the workspace. This is your central device.
    - From "End Devices," add several PCs (e.g., four or five) and arrange them in a star shape around the switch.
    - Connect each PC to the central switch using `Copper Straight-Through` cables.

2.  **Configure IP Addresses:**
    - Assign a unique static IP address to each PC, all within the same subnet.
    - PC0: `192.168.1.10` / `255.255.255.0`
    - PC1: `192.168.1.11` / `255.255.255.0`
    - PC2: `192.168.1.12` / `255.255.255.0`
    - ...and so on.

3.  **Run the Simulation:**
    - Switch to "Simulation" mode and ensure the "ICMP" filter is selected.
    - Use the "Add Simple PDU" tool to send a packet from one PC to another.
    - Click "Capture / Forward" to observe the data flow.

**What to Observe:**
The packet travels from the source PC directly to the central switch. The switch then forwards the packet **only** to the destination PC (after an initial ARP broadcast to learn MAC addresses, as seen in the previous tutorial).

- **Key Advantage:** If one PC's cable fails, only that PC is affected. The rest of the network continues to function.
- **Key Disadvantage:** If the central switch fails, the entire network goes down.

---

#### B) Bus Topology Simulation

In a bus topology, all devices are connected to a single main cable, called the bus. This is a legacy topology, and Packet Tracer simulates it using a hub or coaxial cable. Using a hub is a more modern representation of the shared bus concept.

**Simulation Steps:**

1.  **Build the Topology:**
    - From the "Network Devices" menu, select "Hubs" and drag a `Hub-PT` into the workspace.
    - Add several PCs and connect them all to the hub using `Copper Straight-Through` cables. This functionally simulates a bus where all devices share the same communication medium.
    - _(For a more traditional look, you could use coaxial cables ("Connections" -> "Coaxial") with T-connectors and terminators, but a hub is simpler for observing the logic)._

2.  **Configure IP Addresses:**
    - Assign unique IP addresses to each PC within the same subnet (e.g., `192.168.1.10`, `192.168.1.11`, etc.).

3.  **Run the Simulation:**
    - Go to "Simulation" mode.
    - Send a simple PDU from a PC at one end to a PC at the other end.
    - Click "Capture / Forward."

**What to Observe:**
The packet is sent from the source PC to the hub. The hub, acting as a shared bus, broadcasts the packet to **every other device** on the network. This creates a lot of unnecessary traffic and shows how collisions can occur (though Packet Tracer manages them).

- **Key Disadvantage:** If the main cable (or the hub) fails, the entire network is disabled. All traffic is visible to all devices, creating a security concern.

---

#### C) Ring Topology Simulation

In a true ring topology, each device is connected to exactly two other devices, forming a circular pathway for data. Packets travel from node to node in one direction. Physical ring topologies (like FDDI) are rare now. You can simulate the _logical_ flow in Packet Tracer.

**Simulation Steps:**

1.  **Build the Topology:**
    - There isn't a single "ring" device. You create the ring structure manually.
    - Add three `2960` switches to the workspace, arranging them in a triangle.
    - Connect Switch0 to Switch1, Switch1 to Switch2, and Switch2 back to Switch0 using `Copper Cross-Over` cables (dashed black line) to form a ring.
    - Connect one PC to each switch using `Copper Straight-Through` cables.

2.  **Configure IP Addresses:**
    - Assign IPs to the PCs, all in the same subnet (e.g., `192.168.1.10`, `192.168.1.11`, `192.168.1.12`).

3.  **Run the Simulation:**
    - Go to "Simulation" mode.
    - Send a simple PDU from PC0 to PC2.
    - Click "Capture / Forward."

**What to Observe:**
Because of how switches work with Spanning Tree Protocol (STP) to prevent loops, one of the switch-to-switch links will be automatically blocked (you'll see an amber light on one port). This breaks the physical ring to prevent a broadcast storm. The packet will travel the non-blocked path. While this doesn't perfectly simulate a token-passing ring, it demonstrates how modern networks prevent the loops that ring topologies create. To simulate the "one-way" travel, you would have to manually disconnect one of the links to force traffic to go the long way around.

---

#### D) Mesh Topology Simulation

In a mesh topology, devices are interconnected, providing multiple paths for data. In a **full mesh**, every device is connected to every other device. In a **partial mesh**, only some devices are fully interconnected.

**Simulation Steps (Partial Mesh with Routers):**

1.  **Build the Topology:**
    - Add three `1941` routers to the workspace.
    - Connect them to each other in a triangle. Use "Connections" and select "Automatically choose connection type" for simplicity, or use Serial cables if you want to configure those interfaces.
    - Add a switch to each router, and then connect a PC to each switch. This gives you three separate networks connected in a mesh.

2.  **Configure IP Addresses & Routing:**
    - This is more complex. Each connection between routers needs its own subnet (e.g., R1-R2 is `10.0.1.0/24`, R2-R3 is `10.0.2.0/24`, R3-R1 is `10.0.3.0/24`).
    - Each LAN (PC-Switch-Router) needs its own subnet (e.g., LAN1 is `192.168.1.0/24`, LAN2 is `192.168.2.0/24`, LAN3 is `192.168.3.0/24`).
    - You must configure a **routing protocol** (like RIP or OSPF) on all routers so they can learn about the different paths.
      - On each router's CLI: `router rip`, then `network [network-address]` for each directly connected network.

3.  **Run the Simulation:**
    - Go to "Simulation" mode and send a PDU from a PC in one LAN to a PC in another.
    - Now, delete the direct link between two routers (e.g., click the "Delete" tool and click the cable between R1 and R2).
    - Send another PDU between the same two PCs.

**What to Observe:**
The first packet will take the shortest path. After you delete the direct link, the routing protocol will reconverge, and the routers will find the next-best path. The second packet will now travel around the longer path, demonstrating the redundancy and fault tolerance of a mesh network.

---

#### E) Tree & Hybrid Topologies

- **Tree Topology (Hierarchical):** This is essentially a series of interconnected star topologies.
  - **Simulation:** Place one "core" switch at the top. Connect it to two "distribution" switches below it. Then, connect several PCs to each of the distribution switches. This creates a hierarchy, common in larger networks. Communication between PCs on different distribution switches must go up to the core switch and back down.

- **Hybrid Topology:** This is any combination of two or more different topologies. For example, connecting two star networks and a bus network.
  - **Simulation:** Create a star network with a switch and several PCs. Create another star network. Connect the two switches. Now, add a hub and connect it to one of the switches. Connect a few more PCs to the hub. You have now created a Star-Bus-Star hybrid topology. Sending a packet from a PC on the hub will result in a broadcast within that bus segment, but will be forwarded intelligently once it reaches the switched portion of the network.
