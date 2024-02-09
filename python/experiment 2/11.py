try:
    
    number = int(input("Enter a number: "))
    shift_count = int(input("Enter the shift count: "))
    
    
    left_shifted = number << shift_count
    right_shifted = number >> shift_count


    print(f"Left-shifted value: {left_shifted}")
    print(f"Right-shifted value: {right_shifted}")

except ValueError as e:
    print(f"Error: {e}")
