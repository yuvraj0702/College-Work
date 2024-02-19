def dec_bin(num):
    if num == 0:
        return '0'
    
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    
    return binary

decimal_number = int(input("Enter a decimal number: "))
binary_representation = dec_bin(decimal_number)
print("Binary representation:", binary_representation)
