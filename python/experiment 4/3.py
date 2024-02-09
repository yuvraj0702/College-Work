
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1

    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b

    return fib_series


terms = 10  
result = fibonacci_series(terms)

print(f"The Fibonacci series up to {terms} terms is: {result}")
