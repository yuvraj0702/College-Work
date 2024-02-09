
try:
    string_input = input("Enter a string: ")
    char_to_check = input("Enter a character to check in the string: ")
    
    
    if char_to_check in string_input:
        print(f"{char_to_check} is in the string.")
    else:
        print(f"{char_to_check} is not in the string.")

except ValueError as e:
    print(f"Error: {e}")
