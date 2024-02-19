def sum_numbers(*args):
    sum = 0  
    
    
    for num in args:
        sum += num  
    
    return sum  

print(sum_numbers(1, 2, 3))       
print(sum_numbers(5, 20, 15, 20,100)) 
print(sum_numbers(2, 4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))