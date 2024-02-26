def calculate_average(n, values):
    total = sum(values)
    average = total / n
    return average

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the number of values: "))
    
    # Input values
    values = tuple(float(input(f"Enter value {i + 1}: ")) for i in range(n))
    
    avg = calculate_average(n, values)
    print("Average of the values:", avg)
