def xor(a, b):
    result = []
    for i in range(len(b)):
        result.append(str(int(a[i]) ^ int(b[i])))
    return ''.join(result)

def divide(data, divisor):
    pick = len(divisor)
    tmp = data[:pick]
    
    while pick < len(data):
        if tmp[0] == '1':
            tmp = xor(tmp, divisor) + data[pick]
        else:
            tmp = xor(tmp, '0' * pick) + data[pick]
        pick += 1
    
    if tmp[0] == '1':
        tmp = xor(tmp, divisor)
    else:
        tmp = xor(tmp, '0' * len(divisor))
    
    return tmp.zfill(len(divisor) - 1)

def encode_data(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = divide(appended_data, key)
    return data + remainder

def detect_error(received_data, key):
    remainder = divide(received_data, key)
    return remainder == '0' * (len(key) - 1)

data = '1011001'
key = '1101'

print("Original Data:", data)
encoded_data = encode_data(data, key)
print("Encoded Data to be Transmitted:", encoded_data)

error_data = list(encoded_data)
error_data[3] = '1' if error_data[3] == '0' else '0'
error_data = ''.join(error_data)
print("Received Data with Error:", error_data)

if detect_error(error_data, key):
    print("No error detected in the received message.")
else:
    print("Error detected in the received message.")
