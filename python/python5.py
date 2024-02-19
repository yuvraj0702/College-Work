
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage:
num_terms = int(input("Enter the number of terms in Fibonacci series: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for i in range(num_terms):
        print(fibonacci_recursive(i))

''''''
