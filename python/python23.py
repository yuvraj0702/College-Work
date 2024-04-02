def print_natural_numbers():
    count = 0
    while True:
        yield count
        count += 1
        if count == 20:
            raise StopIteration

try:
    numbers_generator = print_natural_numbers()
    while True:
        print(next(numbers_generator))
except StopIteration:
    print("Displayed first 20 numbers. Exiting the program.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")