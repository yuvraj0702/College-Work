def is_palindrome(number):
    
    num_str = str(number)
    
    
    return num_str == num_str[::-1]


number = 121  
result = is_palindrome(number)

if result:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
