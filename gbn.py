import time
import random

class GoBackN:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        self.sender_window_base = 0
        self.next_seq_num = 0
        self.receiver_expected_num = 0
        self.frames_sent = []
        self.frames_received = []

    def simulate(self):
        print("Go-Back-N Protocol Simulation: ")
        print(f"Window Size: {self.window_size}, Total Frames to Send: {self.total_frames}\n")

        while self.sender_window_base < self.total_frames:
            self.send_frames()
            ack = self.receive_frames()
            self.process_acknowledgment(ack)
            time.sleep(1)

        print("\n--- Simulation Complete ---")
        print(f"Total frames successfully sent and received: {len(self.frames_received)}")
        print(f"Final received frames sequence: {self.frames_received}")

    def send_frames(self):
        """Sender sends all frames within its current window."""
        while self.next_seq_num < self.sender_window_base + self.window_size and self.next_seq_num < self.total_frames:
            print(f"SENDER: Sending frame {self.next_seq_num}...")
            self.frames_sent.append(self.next_seq_num)
            self.next_seq_num += 1

    def receive_frames(self):
        """
        Receiver processes incoming frames.
        Simulates a frame being lost occasionally.
        """
        if self.sender_window_base < self.total_frames and random.randint(1, 10) <= 2: # 20% chance of frame loss
            print(f"\nTRANSMISSION: Frame {self.receiver_expected_num} was lost!\n")
            return self.receiver_expected_num - 1
        
        ack_to_send = -1
        for frame_num in self.frames_sent:
             if frame_num == self.receiver_expected_num:
                 print(f"RECEIVER: Received frame {frame_num} correctly. Sending ACK {frame_num}.")
                 self.frames_received.append(frame_num)
                 self.receiver_expected_num += 1
                 ack_to_send = frame_num
             else:
                 print(f"RECEIVER: Received out-of-order frame {frame_num}. Discarding. Resending ACK {self.receiver_expected_num - 1}.")
        
        self.frames_sent.clear()
        return ack_to_send


    def process_acknowledgment(self, ack):
        """
        Sender slides its window based on the received ACK.
        If a timeout is detected (simulated by a duplicate/old ACK), it goes back.
        """
        if ack + 1 > self.sender_window_base:
            print(f"SENDER: Received ACK {ack}. Sliding window base to {ack + 1}.\n")
            self.sender_window_base = ack + 1
            if self.sender_window_base == self.next_seq_num:
                pass
        else:
            # This simulates a timeout or a lost frame scenario
            print(f"\nSENDER: Timeout or duplicate ACK received (ACK {ack}).")
            print(f"SENDER: --- GOING BACK N --- Resending frames from {self.sender_window_base}.\n")
            self.next_seq_num = self.sender_window_base # Reset next_seq_num to go back

if __name__ == "__main__":
    WINDOW_SIZE = 4
    TOTAL_FRAMES = 15

    protocol = GoBackN(window_size=WINDOW_SIZE, total_frames=TOTAL_FRAMES)
    protocol.simulate()
