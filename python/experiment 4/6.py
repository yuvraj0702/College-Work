def sum_of_digits(number):

    digit_sum = 0

    
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number = number // 10

    return digit_sum

number = 12345  
result = sum_of_digits(number)

print(f"The sum of digits in {number} is: {result}")
