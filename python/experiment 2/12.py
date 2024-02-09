
sequence = (10, 20, 56, 78, 89)


try:
    number = int(input("Enter a number to check in the sequence: "))
    

    if number in sequence:
        print(f"{number} is in the sequence.")
    else:
        print(f"{number} is not in the sequence.")

except ValueError as e:
    print(f"Error: {e}")
