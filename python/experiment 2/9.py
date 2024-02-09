try:
    
    n = int(input("Enter a positive integer (n): "))
    
    if n <= 0:
        raise ValueError("Please enter a positive integer.")
    
    
    sum_natural_numbers = n * (n + 1) // 2

    
    print(f"The sum of the first {n} natural numbers is: {sum_natural_numbers}")

except ValueError as e:
    print(f"Error: {e}")
