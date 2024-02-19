# write a program to demonstrate variable length argument
def is_prime(*args):
    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = []
    for num in args:
        if check_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage:
numbers = map(int, input("Enter numbers to check for primality (separated by space): ").split())
prime_numbers = is_prime(*numbers)

if prime_numbers:
    print("Prime numbers:", prime_numbers)
else:
    print("No prime numbers found.")
