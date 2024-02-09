def print_multiplication_table(number, table_range):
    for i in range(1, table_range + 1):
        result = number * i
        print(f"{number} * {i} = {result}")


given_number = 5
table_range = 10  

print(f"Multiplication table for {given_number} up to {table_range}:\n")
print_multiplication_table(given_number, table_range)
