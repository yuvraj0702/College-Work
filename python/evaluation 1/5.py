

def calc_gcd_recursive(a, b):
    
    if b == 0:
        return a
    else:
        return calc_gcd_recursive(b, a % b)


num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

result = calc_gcd_recursive(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")