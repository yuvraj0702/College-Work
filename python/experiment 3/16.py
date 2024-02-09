try:
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    
    if num1 > num2:
        print(f"{num1} is the greatest.")
    elif num1 < num2:
        print(f"{num2} is the greatest.")
    else:
        print("Numbers are equal.")

except ValueError as e:
    print(f"Error: {e}")
