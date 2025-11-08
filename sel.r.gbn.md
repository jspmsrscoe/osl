### 6) Go-Back-N and Selective Repeat (Sliding Window Protocols)

Sliding Window Protocols are essential for reliable data transfer over unreliable networks (like the internet). They allow a sender to transmit multiple packets (a "window") before needing to wait for an acknowledgment (ACK), which significantly improves efficiency.

Here, we'll look at the logic and provide simplified Python programs to simulate the behavior of two key sliding window protocols: Go-Back-N and Selective Repeat.

---

#### A) Go-Back-N (GBN) Protocol

In Go-Back-N, the sender can transmit up to `N` frames without receiving an ACK. However, the receiver is very strict: it will only accept frames in the correct sequential order.

**How GBN Works:**

- **Sender:** Maintains a window of size `N`. It sends all frames in its window and starts a single timer for the oldest unacknowledged frame.
- **Receiver:** Only keeps track of the _next expected frame number_. If a frame with that number arrives, it accepts it and sends a cumulative ACK for that number. A cumulative ACK (e.g., `ACK 3`) means "I have received everything up to frame 2 and am now expecting frame 3."
- **Lost Frame Scenario:**
  1.  Sender sends frames 0, 1, 2, 3.
  2.  Frame 2 gets lost.
  3.  Receiver gets frame 0 (sends ACK 1), gets frame 1 (sends ACK 2).
  4.  Receiver gets frame 3, but it was expecting frame 2. **It discards frame 3**. It continues to send ACK 2.
  5.  The sender's timer for frame 2 expires. The sender receives no ACK 3.
  6.  The sender **goes back** to frame 2 and re-transmits it, along with every frame that came after it (frame 3, etc.). This is the key "Go-Back-N" behavior.

**Python Program for Go-Back-N Simulation**

This program simulates the GBN logic. You can set which frame to "lose" to see the re-transmission happen.

```python
import time
import random

# --- Simulation Settings ---
WINDOW_SIZE = 4
TOTAL_FRAMES = 10
TIMEOUT = 2  # Seconds
FRAME_TO_LOSE = 3 # Set to a frame number to simulate its loss

# --- Sender State ---
base = 0 # The oldest unacknowledged frame
next_seq_num = 0 # The next frame to send
sent_frames = {} # Store sent times for timeout checks

# --- Receiver State ---
expected_seq_num = 0
received_frames = []

def sender():
    global base, next_seq_num
    print("--- SENDER START ---")

    while base < TOTAL_FRAMES:
        # Send frames within the window
        while next_seq_num < base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
            print(f"SENDER: Sending frame {next_seq_num}...")
            sent_frames[next_seq_num] = time.time()
            # Simulate sending to the receiver
            receiver(next_seq_num)
            next_seq_num += 1
            time.sleep(0.1) # Small delay for realism

        # Check for timeouts
        if base in sent_frames and time.time() - sent_frames[base] > TIMEOUT:
            print(f"\nSENDER: Timeout for frame {base}! Going back to {base}.\n")
            # Go back N: Reset next_seq_num to base to re-send all frames in window
            next_seq_num = base
            # Clear the sent times for the frames to be re-sent
            for i in range(base, base + WINDOW_SIZE):
                if i in sent_frames:
                    del sent_frames[i]
            continue # Restart the loop to re-send

        # This part would normally be triggered by an incoming ACK
        # Here we simulate it based on the receiver's state
        if expected_seq_num > base:
            print(f"SENDER: Received ACK up to {expected_seq_num - 1}. Updating base from {base} to {expected_seq_num}.")
            base = expected_seq_num

    print("--- SENDER FINISHED ---")


def receiver(seq_num):
    global expected_seq_num
    print(f"\tRECEIVER: Received frame {seq_num}.")

    # Simulate losing a specific frame
    if seq_num == FRAME_TO_LOSE and FRAME_TO_LOSE not in received_frames:
        print(f"\tRECEIVER: >>> Frame {seq_num} was LOST! <<<")
        # In a real scenario, the receiver does nothing here.
        return

    # If the received frame is the one we expect
    if seq_num == expected_seq_num:
        print(f"\tRECEIVER: Frame {seq_num} is correct. Accepting.")
        received_frames.append(seq_num)
        expected_seq_num += 1
        print(f"\tRECEIVER: Sending ACK for next frame ({expected_seq_num}).")
    else:
        # Discard out-of-order frames
        print(f"\tRECEIVER: Frame {seq_num} is out of order. Expected {expected_seq_num}. Discarding.")
        print(f"\tRECEIVER: Re-sending ACK for next expected frame ({expected_seq_num}).")


# --- Run the Simulation ---
print("Starting Go-Back-N Simulation...")
sender()
print("\nFinal received frames:", received_frames)
if len(received_frames) == TOTAL_FRAMES:
    print("SUCCESS: All frames received correctly.")
else:
    print("FAILURE: Not all frames were received.")
```

---

#### B) Selective Repeat Protocol

Selective Repeat is more efficient than GBN. It allows the receiver to accept and buffer out-of-order frames. The sender only re-transmits the specific frames that were lost, not the entire window.

**How Selective Repeat Works:**

- **Sender:** Maintains a window of size `N`. It has a separate timer for each frame it sends.
- **Receiver:** Also maintains a window of size `N`. It accepts any frame that falls within its window, even if it's out of order, and buffers it. It sends a selective ACK (SACK) for the specific frame it received.
- **Lost Frame Scenario:**
  1.  Sender sends frames 0, 1, 2, 3.
  2.  Frame 2 gets lost.
  3.  Receiver gets frame 0 (sends SACK 0), gets frame 1 (sends SACK 1).
  4.  Receiver gets frame 3. Since 3 is within its window, **it accepts and buffers frame 3**. It sends SACK 3.
  5.  The sender's timer for frame 2 expires. It receives no SACK 2.
  6.  The sender re-transmits **only frame 2**.
  7.  When the receiver gets frame 2, it can now deliver the buffered frames (2 and 3) to the upper layer in the correct order.

**Python Program for Selective Repeat Simulation**

This simulation demonstrates the buffering and selective re-transmission logic.

```python
import time
import random

# --- Simulation Settings ---
WINDOW_SIZE = 4
TOTAL_FRAMES = 10
TIMEOUT = 2
FRAMES_TO_LOSE = [3, 6] # A list of frames to simulate losing

# --- Sender State ---
send_base = 0
next_seq_num = 0
sent_frames_timers = {} # Store sent time for each frame: {seq_num: time}
acked_frames = [False] * TOTAL_FRAMES

# --- Receiver State ---
receive_base = 0
received_buffer = {} # Buffer for out-of-order frames: {seq_num: frame_data}

def sender():
    global send_base, next_seq_num
    print("--- SENDER START ---")

    while send_base < TOTAL_FRAMES:
        # Send new frames within the window
        while next_seq_num < send_base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
            print(f"SENDER: Sending frame {next_seq_num}...")
            sent_frames_timers[next_seq_num] = time.time()
            receiver(next_seq_num)
            next_seq_num += 1
            time.sleep(0.1)

        # Check for timeouts on all un-acked frames in the window
        for seq_num in range(send_base, next_seq_num):
            if not acked_frames[seq_num] and time.time() - sent_frames_timers.get(seq_num, 0) > TIMEOUT:
                print(f"\nSENDER: Timeout for frame {seq_num}! Re-sending ONLY frame {seq_num}.\n")
                # Re-send only the timed-out frame
                sent_frames_timers[seq_num] = time.time()
                receiver(seq_num)

        # Slide window forward if the base frame has been acked
        while send_base < TOTAL_FRAMES and acked_frames[send_base]:
            send_base += 1
            print(f"SENDER: Window base sliding to {send_base}.")

    print("--- SENDER FINISHED ---")


def receiver(seq_num):
    global receive_base
    print(f"\tRECEIVER: Received frame {seq_num}.")

    # Simulate losing specific frames
    if seq_num in FRAMES_TO_LOSE and seq_num not in received_buffer and not acked_frames[seq_num]:
        print(f"\tRECEIVER: >>> Frame {seq_num} was LOST! <<<")
        FRAMES_TO_LOSE.remove(seq_num) # Lose it only once
        return

    # Check if the frame is within the receiver's window
    if receive_base <= seq_num < receive_base + WINDOW_SIZE:
        print(f"\tRECEIVER: Frame {seq_num} is within window. Sending SACK {seq_num}.")
        # Simulate sending SACK back to sender
        sender_receives_ack(seq_num)

        if seq_num == receive_base:
            # This is the expected in-order frame, deliver it
            receive_base += 1
            # Check buffer for consecutive frames that can now be delivered
            while receive_base in received_buffer:
                del received_buffer[receive_base]
                receive_base += 1
            print(f"\tRECEIVER: Delivered frames. Window base is now {receive_base}.")
        else:
            # Buffer the out-of-order frame
            print(f"\tRECEIVER: Frame {seq_num} is out of order. Buffering.")
            received_buffer[seq_num] = "data" # Store frame data
    else:
        print(f"\tRECEIVER: Frame {seq_num} is outside window ({receive_base} to {receive_base + WINDOW_SIZE - 1}). Discarding.")

def sender_receives_ack(seq_num):
    print(f"SENDER: Received SACK for frame {seq_num}.")
    acked_frames[seq_num] = True


# --- Run the Simulation ---
print("Starting Selective Repeat Simulation...")
sender()
print(f"\nSUCCESS: All frames acked by sender.")

```
