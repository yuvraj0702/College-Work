def calc_exp(base, exp):

    result = 1
    for i in range(exp):
        result *= base
    return result

# Test the function
base = float(input("Enter the base number: "))
exp = int(input("Enter the exponent (greater than 0): "))

while exp <= 0:
    print("Exponent must be greater than 0.")
    exp = int(input("Enter the exponent (greater than 0): "))

result = calc_exp(base, exp)
print(f"The result of {base}^{exp} is:", result)