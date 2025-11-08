import time

WINDOW_SIZE = 4
TOTAL_FRAMES = 10
TIMEOUT = 2
FRAMES_TO_LOSE = [3, 6]

send_base = 0
next_seq_num = 0
sent_frames_timers = {}
acked_frames = [False] * TOTAL_FRAMES

receive_base = 0
received_buffer = {}


def sender():
    global send_base, next_seq_num
    print("--- SENDER START ---")

    while send_base < TOTAL_FRAMES:
        while next_seq_num < send_base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
            print(f"SENDER: Sending frame {next_seq_num}...")
            sent_frames_timers[next_seq_num] = time.time()
            receiver(next_seq_num)
            next_seq_num += 1
            time.sleep(0.1)

        for seq_num in range(send_base, next_seq_num):
            if (
                not acked_frames[seq_num]
                and time.time() - sent_frames_timers.get(seq_num, 0) > TIMEOUT
            ):
                print(
                    f"\nSENDER: Timeout for frame {seq_num}! Re-sending ONLY frame {
                        seq_num
                    }.\n"
                )
                sent_frames_timers[seq_num] = time.time()
                receiver(seq_num)

        while send_base < TOTAL_FRAMES and acked_frames[send_base]:
            send_base += 1
            print(f"SENDER: Window base sliding to {send_base}.")

    print("--- SENDER FINISHED ---")


def receiver(seq_num):
    global receive_base
    print(f"\tRECEIVER: Received frame {seq_num}.")

    if (
        seq_num in FRAMES_TO_LOSE
        and seq_num not in received_buffer
        and not acked_frames[seq_num]
    ):
        print(f"\tRECEIVER: >>> Frame {seq_num} was LOST! <<<")
        FRAMES_TO_LOSE.remove(seq_num)
        return

    if receive_base <= seq_num < receive_base + WINDOW_SIZE:
        print(f"\tRECEIVER: Frame {seq_num} is within window. Sending SACK {seq_num}.")
        sender_receives_ack(seq_num)

        if seq_num == receive_base:
            receive_base += 1
            while receive_base in received_buffer:
                del received_buffer[receive_base]
                receive_base += 1
            print(f"\tRECEIVER: Delivered frames. Window base is now {receive_base}.")
        else:
            print(f"\tRECEIVER: Frame {seq_num} is out of order. Buffering.")
            received_buffer[seq_num] = "data"
    else:
        print(
            f"\tRECEIVER: Frame {seq_num} is outside window ({receive_base} to {
                receive_base + WINDOW_SIZE - 1
            }). Discarding."
        )


def sender_receives_ack(seq_num):
    print(f"SENDER: Received SACK for frame {seq_num}.")
    acked_frames[seq_num] = True


print("Starting Selective Repeat Simulation...")
sender()
print("\nSUCCESS: All frames acked by sender.")
