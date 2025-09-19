import time
import random

class StopAndWaitARQ:
    def __init__(self, total_frames):
        self.total_frames = total_frames
        self.frames_to_send = list(range(total_frames))
        self.current_frame_index = 0
        self.seq_num = 0  # Sequence number (0 or 1)
        self.ack_num = 0  # Expected acknowledgment number
        self.timeout_duration = 3.0 # in seconds

    def simulate(self):
        """Main simulation loop."""
        print("--- Stop-and-Wait ARQ Protocol Simulation ---")
        print(f"Total frames to send: {self.total_frames}\n")

        while self.current_frame_index < self.total_frames:
            self.send_frame()
            
            # Wait for acknowledgment
            ack_received = self.wait_for_ack()

            if ack_received:
                print(f"SENDER: ACK {self.ack_num} received successfully.\n")
                # Flip sequence and ack numbers for the next frame
                self.seq_num = 1 - self.seq_num
                self.ack_num = 1 - self.ack_num
                self.current_frame_index += 1
            else:
                # Timeout occurred
                print(f"\nSENDER: Timeout! ACK for frame {self.current_frame_index} with seq {self.seq_num} not received.")
                print("SENDER: --- Retransmitting frame ---\n")
        
        print("--- Simulation Complete ---")
        print("All frames have been successfully sent and acknowledged.")

    def send_frame(self):
        """Sender sends the current frame."""
        print(f"SENDER: Sending frame {self.current_frame_index} with sequence number {self.seq_num}.")
        self.last_sent_time = time.time()

    def receiver(self, seq_num_sent):
        """
        Simulates the receiver's logic.
        Returns the ACK number to be sent back.
        Returns -1 to simulate a lost ACK.
        """
        # 10% chance of the frame being lost in transit
        if random.randint(1, 10) == 1:
            print("TRANSMISSION: Frame was lost!")
            return None # Frame never arrives at receiver

        print(f"RECEIVER: Received frame with sequence number {seq_num_sent}.")

        # If the received sequence number is what the receiver expects
        if seq_num_sent == self.ack_num:
            print(f"RECEIVER: Frame is correct. Accepting data.")
            ack_to_send = self.ack_num
            print(f"RECEIVER: Sending ACK {ack_to_send}.")
            
            # 20% chance of the ACK being lost in transit
            if random.randint(1, 5) == 1:
                print("TRANSMISSION: ACK was lost!")
                return None # ACK is lost
            return ack_to_send
        else:
            # Received a duplicate frame
            print(f"RECEIVER: Duplicate frame detected. Discarding.")
            # Resend ACK for the last correctly received frame
            previous_ack = 1 - self.ack_num
            print(f"RECEIVER: Resending ACK {previous_ack}.")
            return previous_ack

    def wait_for_ack(self):
        """
        Sender waits for an acknowledgment.
        Simulates the waiting period and potential for timeouts.
        """
        while time.time() - self.last_sent_time < self.timeout_duration:
            # In a real network, this would be an event-driven process.
            # Here, we simulate it by immediately calling the receiver.
            
            ack = self.receiver(self.seq_num)
            
            if ack is not None and ack == self.ack_num:
                # Correct ACK received
                return True
                
            # Sleep to simulate network delay and passage of time
            time.sleep(0.5)
        
        # If the loop finishes without returning, a timeout has occurred
        return False

if __name__ == "__main__":
    # Configuration
    TOTAL_FRAMES = 5

    # Create and run the simulation
    protocol = StopAndWaitARQ(total_frames=TOTAL_FRAMES)
    protocol.simulate()
