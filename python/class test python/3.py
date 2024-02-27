def binary_to_decimal(binary_str):
    decimal_num = 0
    power = len(binary_str) - 1
    
    for digit in binary_str:
        decimal_num += int(digit) * (2 ** power)
        power -= 1
    
    return decimal_num

# Test the function
binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_number)
print("Equivalent decimal number:", decimal_number)
