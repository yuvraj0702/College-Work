try:
    num = float(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative number entered.")
    else:
        print("The number entered is:", num)
except ValueError as ve:
    print("Error:", ve)
except :
    print("An error occurred:")     