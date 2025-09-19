import time
import random

class SelectiveRepeat:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        
        self.sender_base = 0
        self.next_seq_num = 0
        self.sender_buffer = {}
        
        self.receiver_base = 0
        self.receiver_buffer = {}
        self.received_frames_final = []

    def simulate(self):
        """Main simulation loop."""
        print("--- Selective Repeat Protocol Simulation ---")
        print(f"Window Size: {self.window_size}, Total Frames to Send: {self.total_frames}\n")

        while self.sender_base < self.total_frames:
            self.send_frames()

            acks_to_send = self.receive_frames()
            
            self.process_acknowledgments(acks_to_send)
            
            self.check_timeouts()

            time.sleep(1)

        print("\n--- Simulation Complete ---")
        print(f"Total frames successfully sent and received: {len(self.received_frames_final)}")
        print(f"Final received frames sequence: {sorted(self.received_frames_final)}")

    def send_frames(self):
        """Sender sends frames within the window that haven't been sent/acked yet."""
        while self.next_seq_num < self.sender_base + self.window_size and self.next_seq_num < self.total_frames:
            if self.next_seq_num not in self.sender_buffer or self.sender_buffer[self.next_seq_num] == 'timed_out':
                print(f"SENDER: Sending frame {self.next_seq_num}...")
                self.sender_buffer[self.next_seq_num] = {'status': 'sent', 'time': time.time()}
            self.next_seq_num += 1

    def receive_frames(self):
        """
        Receiver processes incoming frames.
        Simulates frames being lost or arriving out of order.
        """
        arrived_frames = []
        for seq_num, data in self.sender_buffer.items():
            if data['status'] == 'sent':
                if random.randint(1, 10) > 2:
                    arrived_frames.append(seq_num)
                else:
                    print(f"TRANSMISSION: Frame {seq_num} was lost!")
        
        random.shuffle(arrived_frames)
        
        acks = []
        for frame_num in arrived_frames:
            print(f"RECEIVER: Received frame {frame_num}.")
            
            if self.receiver_base <= frame_num < self.receiver_base + self.window_size:
                acks.append(frame_num)
                print(f"RECEIVER: Sending ACK for frame {frame_num}.")
                
                if frame_num == self.receiver_base:
                    self.received_frames_final.append(frame_num)
                    self.receiver_base += 1
                    while self.receiver_base in self.receiver_buffer:
                        self.received_frames_final.append(self.receiver_base)
                        del self.receiver_buffer[self.receiver_base]
                        self.receiver_base += 1
                    print(f"RECEIVER: Window base moved to {self.receiver_base}")
                else:
                    if frame_num not in self.received_frames_final:
                         self.receiver_buffer[frame_num] = True
                         print(f"RECEIVER: Frame {frame_num} is out of order. Buffering.")
            else:
                 print(f"RECEIVER: Discarding frame {frame_num} (outside window).")

        return acks

    def process_acknowledgments(self, acks):
        """Sender marks frames as acknowledged and slides its window."""
        if random.randint(1, 10) == 1 and acks:
            lost_ack = random.choice(acks)
            acks.remove(lost_ack)
            print(f"TRANSMISSION: ACK for frame {lost_ack} was lost!")

        for ack in acks:
            if ack in self.sender_buffer and self.sender_buffer[ack]['status'] == 'sent':
                self.sender_buffer[ack]['status'] = 'acked'
                print(f"SENDER: Received ACK {ack}. Frame marked as acknowledged.")
        
        while self.sender_base in self.sender_buffer and self.sender_buffer[self.sender_base]['status'] == 'acked':
            self.sender_base += 1
        print(f"SENDER: Window base is now at {self.sender_base}.\n")

    def check_timeouts(self):
        """Sender checks for frames that have timed out and need retransmission."""
        timeout_duration = 3.0
        current_time = time.time()
        for seq_num, data in self.sender_buffer.items():
            if data['status'] == 'sent' and current_time - data['time'] > timeout_duration:
                print(f"\nSENDER: Timeout for frame {seq_num}! Retransmitting.")
                self.sender_buffer[seq_num]['status'] = 'timed_out' # Mark for retransmission
                self.next_seq_num = self.sender_base # Reset to re-evaluate window

if __name__ == "__main__":
    WINDOW_SIZE = 4
    TOTAL_FRAMES = 10

    protocol = SelectiveRepeat(window_size=WINDOW_SIZE, total_frames=TOTAL_FRAMES)
    protocol.simulate()