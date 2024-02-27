def odd_numbers_descending(a, b):
    odd_numbers = []
    for num in range(b, a - 1, -1):
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

# Test the function
a = int(input("Enter a positive integer a: "))
b = int(input("Enter a positive integer b (greater than a): "))

if b <= a:
    print("Error: b must be greater than a.")
else:
    result = odd_numbers_descending(a, b)
    print("Odd numbers between", a, "and", b, "in descending order:", result)
