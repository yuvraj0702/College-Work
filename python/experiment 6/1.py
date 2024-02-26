def count_occurrences(n):
    # Initialize counts dictionary
    counts = {0: 0, 1: 0, 2: 0, 3: 0}

    # Scan n values
    for _ in range(n):
        value = int(input("Enter a value between 0 and 3: "))
        if value not in range(4):
            print("Invalid input. Please enter a value between 0 and 3.")
            continue
        counts[value] += 1

    # Print the counts
    for key, value in counts.items():
        print(f"Value {key} occurred {value} times.")


# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the number of values to scan: "))
    count_occurrences(n)
