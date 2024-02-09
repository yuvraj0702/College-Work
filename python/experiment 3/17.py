
try:
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the greatest.")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the greatest.")
    else:
        print(f"{num3} is the greatest.")

except ValueError as e:
    print(f"Error: {e}")
