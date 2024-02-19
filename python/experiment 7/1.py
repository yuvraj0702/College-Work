def find_max_min(numbers):
    if not numbers:
        return None, None
    
    max_num = numbers[0]
    min_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
            
    return max_num, min_num

# Example usage:
numbers = [5, 3, 8, 1, 6]
max_num, min_num = find_max_min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
