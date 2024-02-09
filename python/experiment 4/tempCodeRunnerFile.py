def print_multiplication_table(number, table_range):
    for i in range(1, table_range + 1):
        result = number * i
        print(f"{number} * {i} = {result}")
