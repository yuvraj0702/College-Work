def is_palindrome_list(lst):
    # Check if the list is equal to its reverse
    return lst == lst[::-1]

# Example usage:
# myList = [1, 2, 3, 2, 1]
# print(is_palindrome_list(myList))  # Output: True
