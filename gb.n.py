import time

WINDOW_SIZE = 4
TOTAL_FRAMES = 10
TIMEOUT = 2
FRAME_TO_LOSE = 3

base = 0
next_seq_num = 0
sent_frames = {}

expected_seq_num = 0
received_frames = []


def sender():
    global base, next_seq_num
    print("--- SENDER START ---")

    while base < TOTAL_FRAMES:
        while next_seq_num < base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
            print(f"SENDER: Sending frame {next_seq_num}...")
            sent_frames[next_seq_num] = time.time()
            receiver(next_seq_num)
            next_seq_num += 1
            time.sleep(0.1)

        if base in sent_frames and time.time() - sent_frames[base] > TIMEOUT:
            print(f"\nSENDER: Timeout for frame {base}! Going back to {base}.\n")
            next_seq_num = base
            for i in range(base, base + WINDOW_SIZE):
                if i in sent_frames:
                    del sent_frames[i]
            continue

        if expected_seq_num > base:
            print(
                f"SENDER: Received ACK up to {
                    expected_seq_num - 1
                }. Updating base from {base} to {expected_seq_num}."
            )
            base = expected_seq_num

    print("--- SENDER FINISHED ---")


def receiver(seq_num):
    global expected_seq_num, FRAME_TO_LOSE
    print(f"\tRECEIVER: Received frame {seq_num}.")

    if seq_num == FRAME_TO_LOSE and FRAME_TO_LOSE not in received_frames:
        print(f"\tRECEIVER: >>> Frame {seq_num} was LOST! <<<")
        FRAME_TO_LOSE = 10000
        return

    if seq_num == expected_seq_num:
        print(f"\tRECEIVER: Frame {seq_num} is correct. Accepting.")
        received_frames.append(seq_num)
        expected_seq_num += 1
        print(f"\tRECEIVER: Sending ACK for next frame ({expected_seq_num}).")
    else:
        print(
            f"\tRECEIVER: Frame {seq_num} is out of order. Expected {
                expected_seq_num
            }. Discarding."
        )
        print(
            f"\tRECEIVER: Re-sending ACK for next expected frame ({expected_seq_num})."
        )


print("Starting Go-Back-N Simulation...")
sender()
print("\nFinal received frames:", received_frames)
if len(received_frames) == TOTAL_FRAMES:
    print("SUCCESS: All frames received correctly.")
else:
    print("FAILURE: Not all frames were received.")
