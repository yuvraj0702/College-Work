def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Using variable-length argument
result = sum_all(1, 2, 3, 4, 5)
print("Sum:", result)
# Output: Sum: 15
