def sum_of_cubes(n):
    if n <= 0:
        return 0
    
    sum_cubes = 0
    for i in range(1, n):
        sum_cubes += i ** 3
        
    return sum_cubes

# Example usage:
n = 5
result = sum_of_cubes(n)
print("Sum of cubes of positive integers smaller than", n, "is:", result)
