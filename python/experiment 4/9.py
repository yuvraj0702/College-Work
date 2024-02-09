def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
    return prime_numbers


start_range = 1
end_range = 100

result = print_primes_in_range(start_range, end_range)

print(f"Prime numbers between {start_range} and {end_range}:")
print(result)
