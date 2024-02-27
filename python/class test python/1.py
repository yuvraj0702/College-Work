def hex_to_binary(hex_str):
    # Dictionary mapping hexadecimal digits to their binary representation
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # Convert each hexadecimal digit to its binary representation
    binary_str = ''.join(hex_to_bin[digit] for digit in hex_str.upper())

    return binary_str

# Test the function
hex_number = input("Enter a hexadecimal number: ")
binary_number = hex_to_binary(hex_number)
print("Equivalent binary number:", binary_number)