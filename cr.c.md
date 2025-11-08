### 7) Error Detection and Correction using CRC (Cyclic Redundancy Check)

CRC is a powerful and widely used **error-detection** technique. It is important to note that CRC is designed to _detect_ errors, not to _correct_ them. Error correction requires more complex algorithms like Hamming codes.

The core idea of CRC is to treat binary data as a polynomial and use polynomial division to generate a checksum.

**How it Works: The Analogy**

Imagine you and a friend agree on a secret number, say 7.

- **Sender (You):** You want to send the number 145. To make sure it arrives correctly, you divide 145 by 7. The remainder is 5. You send both numbers: the data (145) and the checksum (5).
- **Receiver (Your Friend):** They receive 145 and 5. To check for errors, they also divide 145 by 7. They get a remainder of 5. Since their calculated remainder matches the one you sent, they are confident the data is correct.
- **Error Scenario:** If the data was corrupted in transit to 146, your friend would divide 146 by 7 and get a remainder of 6. Since 6 does not equal the checksum 5 that you sent, they know an error occurred.

CRC works on the same principle but uses binary polynomial division (which is done using XOR operations).

#### Key Components:

- **Dataword:** The original data you want to send (e.g., `1011001`).
- **Generator Polynomial (or Divisor):** A pre-agreed binary number that both the sender and receiver know. The choice of generator determines the robustness of the error detection. A common example is `1001`.
- **Remainder (CRC Checksum):** The result of the binary division. Its length is always one less than the length of the generator.
- **Codeword:** The original dataword with the CRC remainder appended to it. This is what is actually transmitted.

---

#### Steps at the Sender's Side

1.  **Append Zeros:** Append `k-1` zeros to the right of the dataword, where `k` is the number of bits in the generator polynomial.
2.  **Divide:** Perform binary division (using XOR logic) of the new, extended dataword by the generator polynomial.
3.  **Get Remainder:** The remainder from this division is the CRC checksum.
4.  **Create Codeword:** Replace the appended zeros with the CRC checksum. This codeword is then transmitted.

#### Steps at the Receiver's Side

1.  **Receive Codeword:** The receiver gets the codeword.
2.  **Divide:** The receiver divides the entire received codeword by the _same_ generator polynomial.
3.  **Check Remainder:**
    - If the remainder is all zeros, the data is assumed to be error-free. The receiver removes the CRC checksum part and accepts the original dataword.
    - If the remainder is non-zero, an error has been detected. The receiver discards the packet and may request a re-transmission.

---

### Python Program for CRC Simulation

This program demonstrates the complete CRC process: generating the codeword at the sender and verifying it at the receiver.

```python
def xor_division(dividend, divisor):
    """
    Performs binary division using XOR logic.
    Assumes dividend and divisor are strings of '0's and '1's.
    """
    # The number of bits in the divisor
    divisor_len = len(divisor)
    # The current part of the dividend to be processed
    temp_dividend = dividend[0 : divisor_len]

    while divisor_len < len(dividend):
        if temp_dividend[0] == '1':
            # Perform XOR with the divisor
            temp_dividend = ''.join('1' if x != y else '0' for x, y in zip(temp_dividend, divisor))

        # Bring down the next bit from the dividend
        if divisor_len < len(dividend):
            temp_dividend = temp_dividend[1:] + dividend[divisor_len]
            divisor_len += 1

    # Final XOR operation for the last part
    if temp_dividend[0] == '1':
        temp_dividend = ''.join('1' if x != y else '0' for x, y in zip(temp_dividend, divisor))

    # The remainder is the result of the division, excluding the leading bit
    return temp_dividend[1:]

def generate_crc(dataword, generator):
    """Generates the codeword for a given dataword and generator."""
    generator_len = len(generator)
    # 1. Append n-1 zeros to the dataword
    appended_data = dataword + '0' * (generator_len - 1)

    # 2. Calculate the remainder (CRC)
    remainder = xor_division(appended_data, generator)

    # 3. Create the codeword
    codeword = dataword + remainder

    print(f"Dataword:      {dataword}")
    print(f"Generator:     {generator}")
    print(f"Data w/ Zeros: {appended_data}")
    print(f"CRC Remainder:   {remainder}")
    print(f"Codeword Sent: {codeword}")
    return codeword, remainder

def verify_crc(codeword, generator):
    """Verifies the received codeword."""
    print(f"\n--- RECEIVER SIDE ---")
    print(f"Received Codeword: {codeword}")
    print(f"Generator:         {generator}")

    # 1. Divide the codeword by the generator
    remainder = xor_division(codeword, generator)
    print(f"Calculated Remainder: {remainder}")

    # 2. Check if the remainder is all zeros
    if '1' not in remainder:
        print("Result: NO ERROR DETECTED. Data is accepted.")
        return True
    else:
        print("Result: ERROR DETECTED! Data is rejected.")
        return False

# --- Simulation ---

# Shared parameters
data_to_send = "1011001"
generator_poly = "1001" # Represents x^3 + 1

# --- SENDER ---
print("--- SENDER SIDE ---")
transmitted_codeword, crc_checksum = generate_crc(data_to_send, generator_poly)

# --- TRANSMISSION ---
print("\n...Data is transmitted over the network...")

# --- RECEIVER (Case 1: No Error) ---
verify_crc(transmitted_codeword, generator_poly)

# --- RECEIVER (Case 2: With Error) ---
# Let's introduce an error into the codeword (flip a bit)
error_bit_position = 4
corrupted_codeword_list = list(transmitted_codeword)
corrupted_codeword_list[error_bit_position] = '1' if transmitted_codeword[error_bit_position] == '0' else '0'
corrupted_codeword = "".join(corrupted_codeword_list)

print(f"\n--- Simulating a transmission error at bit {error_bit_position} ---")
verify_crc(corrupted_codeword, generator_poly)
```

**How to Read the Output:**

1.  **Sender Side:** You'll see the original data, how zeros are appended, the calculated CRC, and the final codeword that gets sent.
2.  **Receiver Side (No Error):** The receiver takes the original codeword, divides it, and gets a zero remainder, confirming the data is valid.
3.  **Receiver Side (With Error):** The program manually flips a bit in the codeword. When the receiver divides this corrupted codeword, the remainder is non-zero, which immediately signals that an error has occurred.
