def calculate_redundant_bits(m):
    i = 0
    while (2**i) < (m + i + 1):
        i += 1
    return i

def insert_redundant_bits(data, r):
    j, k = 0, 0
    res = []
    m = len(data)
    total_length = m + r
    
    for i in range(1, total_length + 1):
        if i == 2**j:
            res.append('0')
            j += 1
        else:
            res.append(data[-1 * k])
            k += 1
    
    return ''.join(res[::-1])

def calculate_parity_bits(arr, r):
    n = len(arr)
    arr = list(arr)
    
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val ^= int(arr[-1 * j])
        arr[-(2**i)] = str(val)
    
    return ''.join(arr)

def detect_error(received_data, r):
    n = len(received_data)
    error_position = 0
    
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val ^= int(received_data[-1 * j])
        error_position += val * (2**i)
    
    return error_position

data = '1011001'
print("Original Data:", data)

m = len(data)
r = calculate_redundant_bits(m)

encoded_data = insert_redundant_bits(data, r)

final_encoded_data = calculate_parity_bits(encoded_data, r)
print("Encoded Data to be Transmitted:", final_encoded_data)

error_position_simulated = 3
error_data = list(final_encoded_data)
error_data[-error_position_simulated] = '1' if error_data[-error_position_simulated] == '0' else '0'
error_data = ''.join(error_data)
print("Received Data with Error:", error_data)

error_position = detect_error(error_data, r)
if error_position == 0:
    print("No error detected in the received message.")
else:
    print(f"Error detected at position {len(error_data) - error_position + 1} from the left.")
    corrected_data = list(error_data)
    corrected_data[-error_position] = '1' if corrected_data[-error_position] == '0' else '0'
    corrected_data = ''.join(corrected_data)
    print("Corrected Data:", corrected_data)
