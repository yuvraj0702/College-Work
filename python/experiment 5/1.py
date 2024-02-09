def count_capital_letters(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

def display_capital_letters(string):
    capitals = [char for char in string if char.isupper()]
    return ''.join(capitals)


input_string = input("Enter a string: ")
count = count_capital_letters(input_string)
print("Number of capital letters:", count)

capital_letters = display_capital_letters(input_string)
print("Capital letters in the string:", capital_letters)
