def sum_of_digits_without_recursion(number):
    
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits



def sum_of_digits_with_recursion(number):
    
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits_with_recursion(number // 10)


user_number = int(input("Enter a four-digit number: "))

result_with_recursion = sum_of_digits_with_recursion(user_number)
print(f"The sum of digits with recursion is: {result_with_recursion}")