def find_divisible_numbers(start, end):
    divisible_numbers = []

    for num in range(start, end + 1):
        if num % 5 == 0 or num % 7 == 0:
            divisible_numbers.append(num)

    return divisible_numbers


start_range = 1
end_range = 100

result = find_divisible_numbers(start_range, end_range)

print(f"Numbers divisible by 5 or 7 between {start_range} and {end_range}:")
print(result)
