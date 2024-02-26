def compute_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Create a list of five elements
numbers_list = [10, 20, 30, 40, 50]

# Pass the list to the function and compute the average
average_result = compute_average(numbers_list)

print("Average of the numbers:", average_result)
