def has_duplicates(lst):
    # Convert the list to a set to remove duplicates
    # If the length of the set is equal to the length of the list, there are no duplicates
    return len(set(lst)) != len(lst)

# Example usage:
# myList = [1, 2, 3, 4, 5]
# print(has_duplicates(myList))  # Output: False

# Duplicate example:
# myList = [1, 2, 3, 2, 4, 5]
# print(has_duplicates(myList))  # Output: True
