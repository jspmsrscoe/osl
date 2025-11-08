import random
import time


class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_size = 0
        self.last_leak_time = time.time()

    def _leak(self):
        now = time.time()
        time_elapsed = now - self.last_leak_time

        leaked_packets = int(time_elapsed * self.leak_rate)

        if leaked_packets > 0:
            self.current_size = max(0, self.current_size - leaked_packets)
            self.last_leak_time = now
            print(
                f"LEAK: Leaked {leaked_packets} packets. Current size: {
                    self.current_size
                }"
            )

    def add_packet(self, packet_size):
        self._leak()

        if self.current_size + packet_size <= self.capacity:
            self.current_size += packet_size
            print(
                f"PACKET ADDED (+{packet_size}). Current bucket size: {
                    self.current_size
                }/{self.capacity}"
            )
            return True
        else:
            print(
                f"PACKET DISCARDED! Bucket full. Current size: {self.current_size}/{
                    self.capacity
                }"
            )
            return False


BUCKET_CAPACITY = 10
LEAK_RATE = 2
TOTAL_PACKETS = 25

print("--- Starting Leaky Bucket Simulation ---")
print(f"Bucket Capacity: {BUCKET_CAPACITY}, Leak Rate: {LEAK_RATE} packets/sec\n")

bucket = LeakyBucket(capacity=BUCKET_CAPACITY, leak_rate=LEAK_RATE)

for i in range(TOTAL_PACKETS):
    arrival_interval = random.uniform(0.1, 0.4)
    time.sleep(arrival_interval)

    print(f"\n--- Packet {i + 1} arrives ---")
    bucket.add_packet(packet_size=1)

print("\n--- Simulation Finished ---")
