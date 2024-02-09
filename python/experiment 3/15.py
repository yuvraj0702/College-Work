try:
    
    number = int(input("Enter a number: "))
    
    
    if number % 5 == 0:
        print(f"{number} is a multiple of five.")
    else:
        print(f"{number} is not a multiple of five.")

except ValueError as e:
    print(f"Error: {e}")
