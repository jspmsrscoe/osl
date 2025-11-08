### 14) Leaky Bucket Algorithm

The Leaky Bucket algorithm is a method used for **traffic shaping** and **congestion control**. Its primary purpose is to regulate the flow of data being sent to a network, smoothing out bursty traffic into a steady, predictable stream.

#### The Analogy

Imagine a bucket with a small hole in the bottom.

- **The Bucket:** Represents a finite-sized queue (a buffer) that can hold packets. It has a specific **capacity**.
- **Water Pouring In:** Represents incoming packets arriving at the network interface. These packets can arrive in bursts (like someone dumping a pail of water in) or at an irregular rate.
- **The Hole:** Represents the network's constant output rate. Water leaks out of the hole at a steady, fixed rate, regardless of how much water is in the bucket or how fast it's being poured in.
- **Spilling Over:** If water is poured into the bucket faster than it can leak out, the bucket will eventually fill up. Any new water that is poured in will simply spill over the sides and be lost. This represents **packet loss** (or discarding packets).

#### How the Algorithm Works in Networking

1.  **Packet Arrival:** When a packet arrives, the system checks if there is space in the bucket (the buffer).
2.  **Queueing:**
    - If there is space, the packet is placed in the queue.
    - If the bucket is full, the packet is **discarded**.
3.  **Transmission (The "Leak"):** At a fixed interval (e.g., every clock tick), the system checks if the bucket is empty.
    - If the bucket is not empty, one packet is taken from the queue and transmitted. This output rate is constant and is called the **leak rate**.
    - If the bucket is empty, nothing happens during that interval.

The key takeaway is that no matter how bursty the input traffic is, the output traffic is always a smooth, constant stream. This prevents a sudden flood of packets from overwhelming downstream routers and switches.

---

### Python Program to Simulate the Leaky Bucket Algorithm

This program simulates the leaky bucket logic. We will define the bucket's capacity, the rate at which packets "leak" out, and simulate a series of incoming packets to see how the bucket handles them.

```python
import time
import random

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        """
        Initializes the Leaky Bucket.
        :param capacity: The maximum number of packets the bucket can hold.
        :param leak_rate: The number of packets that are processed per second.
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_size = 0
        self.last_leak_time = time.time()

    def _leak(self):
        """
        Internal method to simulate the leaking of packets over time.
        """
        now = time.time()
        time_elapsed = now - self.last_leak_time

        # Calculate how many packets would have leaked in the elapsed time
        leaked_packets = int(time_elapsed * self.leak_rate)

        if leaked_packets > 0:
            self.current_size = max(0, self.current_size - leaked_packets)
            self.last_leak_time = now
            print(f"LEAK: Leaked {leaked_packets} packets. Current size: {self.current_size}")

    def add_packet(self, packet_size):
        """
        Adds a packet to the bucket and checks for overflow.
        :param packet_size: The size of the incoming packet (we'll use 1 for simplicity).
        :return: True if the packet was added, False if it was discarded.
        """
        # First, let's update the bucket size based on any leaks that happened
        self._leak()

        if self.current_size + packet_size <= self.capacity:
            self.current_size += packet_size
            print(f"PACKET ADDED (+{packet_size}). Current bucket size: {self.current_size}/{self.capacity}")
            return True
        else:
            print(f"PACKET DISCARDED! Bucket full. Current size: {self.current_size}/{self.capacity}")
            return False

# --- Simulation Settings ---
BUCKET_CAPACITY = 10  # Can hold a maximum of 10 packets
LEAK_RATE = 2       # Leaks 2 packets per second
TOTAL_PACKETS = 25  # Total packets to simulate arriving

# --- Run the Simulation ---
print("--- Starting Leaky Bucket Simulation ---")
print(f"Bucket Capacity: {BUCKET_CAPACITY}, Leak Rate: {LEAK_RATE} packets/sec\n")

bucket = LeakyBucket(capacity=BUCKET_CAPACITY, leak_rate=LEAK_RATE)

for i in range(TOTAL_PACKETS):
    # Simulate packets arriving at random intervals (0.1 to 0.6 seconds)
    # A smaller interval means a higher arrival rate (more bursty)
    arrival_interval = random.uniform(0.1, 0.4)
    time.sleep(arrival_interval)

    print(f"\n--- Packet {i+1} arrives ---")
    bucket.add_packet(packet_size=1)

print("\n--- Simulation Finished ---")
```

#### How to Read the Simulation Output:

- **PACKET ADDED:** When you see this, it means an incoming packet arrived and there was enough space in the bucket to queue it.
- **LEAK:** This message appears whenever the `_leak()` method is called and time has passed. It shows that packets are being processed and removed from the queue at a steady rate.
- **PACKET DISCARDED!:** This is the key behavior. You will see this message when packets arrive too quickly (in a burst). The leak rate can't keep up, the bucket fills to its capacity, and any new packets are dropped.

By changing the `BUCKET_CAPACITY`, `LEAK_RATE`, and the `arrival_interval` in the `time.sleep()` call, you can see how the algorithm behaves under different conditions. A lower `arrival_interval` will create a bigger burst and cause more packets to be discarded.
