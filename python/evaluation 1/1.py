def max_of_three(num1=1, num2=2, num3=3):
    

    
    if num1 >= num2 and num1 >= num3:
        return num1
    
    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3

num1 = int(input("Enter first no: "))
num2 = int(input("Enter second no: "))
num3 = int(input("Enter third no: "))
print("Maximum number is:", max_of_three(num1,num2,num3))