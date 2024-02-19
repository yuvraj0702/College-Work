def sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total

# Test the function
n = int(input("Enter a positive integer: "))
result = sum_of_cubes(n)
print("Sum of the cubes of positive integers smaller than", n, "is", result)
