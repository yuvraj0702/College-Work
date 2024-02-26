def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(numbers):
    return list(filter(is_prime, numbers))

# Example usage:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_numbers = get_primes(numbers)
# print(prime_numbers)  # Output: [2, 3, 5, 7]
