def hex_to_bin(hex_str):
    decimal_num = int(hex_str, 16)  # hex to decimal
    binary_str = ""
    while decimal_num > 0:
        binary_str = str(decimal_num % 2) + binary_str
        decimal_num //= 2
    return binary_str

hexadecimal_input = input("Enter a hexadecimal number: ")
binary_output = hex_to_bin(hexadecimal_input)
print("Binary representation is", binary_output)