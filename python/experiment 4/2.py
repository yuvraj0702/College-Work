def is_armstrong_number(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    
    return armstrong_sum == number


number = 153  
result = is_armstrong_number(number)

if result:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
