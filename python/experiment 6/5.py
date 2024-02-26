def split_list(input_list, n):
    # Split the list into two parts
    first_part = input_list[:n]
    second_part = input_list[n:]
    return first_part, second_part

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
first_part, second_part = split_list(my_list, n)
print("First part:", first_part)
print("Second part:", second_part)
