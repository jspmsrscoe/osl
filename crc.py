def xor(a, b):
    """Performs bitwise XOR on two binary strings."""
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    """
    Performs modulo-2 division (binary division with XOR).
    This is the core of the CRC algorithm.
    """
    # Number of bits to be XORed at a time.
    pick = len(divisor)
    # Slicing the dividend to appropriate size for XORing
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            # If the leftmost bit is 1, replace tmp with the result of XOR
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            # If the leftmost bit is 0, XOR with all zeros
            tmp = xor('0' * pick, tmp) + dividend[pick]
        
        # Move to the next bit
        pick += 1

    # For the last n bits, we have to carry it out normally
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

def encode_data(data, key):
    """
    Encodes the data by appending the CRC checksum.
    This is done on the sender's side.
    """
    key_length = len(key)
    # 1. Append n-1 zeros to the data (n is length of key)
    appended_data = data + '0' * (key_length - 1)
    # 2. Perform modulo-2 division
    remainder = mod2div(appended_data, key)
    # 3. Append the remainder (CRC) to the original data
    codeword = data + remainder
    print(f"Sender: Remainder (CRC) is: {remainder}")
    print(f"Sender: Encoded Data (Codeword) to be sent: {codeword}")
    return codeword

def receiver_check(received_data, key):
    """
    Checks the received codeword for errors.
    This is done on the receiver's side.
    """
    # Perform modulo-2 division on the received data
    remainder = mod2div(received_data, key)
    print(f"Receiver: Remainder is: {remainder}")
    # If the remainder is all zeros, the data is correct
    if '1' not in remainder:
        print("Receiver: No error detected. Data is correct.")
    else:
        print("Receiver: Error detected in data.")
        # Note: CRC is an error-detection code, not a correction code.
        # In a real-world scenario, the receiver would now request a retransmission.

if __name__ == "__main__":
    # --- Configuration ---
    # The data to be sent
    data_to_send = "100100"
    # The generator polynomial (CRC key)
    crc_key = "1101"

    print("--- CRC Simulation ---")
    print(f"Original Data: {data_to_send}")
    print(f"Generator Polynomial (Key): {crc_key}\n")

    # --- Sender Side ---
    print("--- Sending Process ---")
    codeword_sent = encode_data(data_to_send, crc_key)
    print("-" * 25, "\n")
    
    # --- Transmission Simulation ---
    # Scenario 1: No error in transmission
    print("--- Receiving Process (Scenario 1: No Error) ---")
    print(f"Data received: {codeword_sent}")
    receiver_check(codeword_sent, crc_key)
    print("-" * 25, "\n")

    # Scenario 2: An error is introduced during transmission
    print("--- Receiving Process (Scenario 2: With Error) ---")
    # Let's flip a bit to simulate an error (e.g., the 3rd bit)
    error_bit_position = 2
    codeword_list = list(codeword_sent)
    codeword_list[error_bit_position] = '1' if codeword_sent[error_bit_position] == '0' else '0'
    codeword_with_error = "".join(codeword_list)
    
    print(f"Original codeword: {codeword_sent}")
    print(f"Codeword with error: {codeword_with_error} (bit at index {error_bit_position} was flipped)")
    receiver_check(codeword_with_error, crc_key)
    print("-" * 25, "\n")