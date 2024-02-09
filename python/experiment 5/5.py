def count_alphabets(string):

    string = string.lower()
    
    
    alphabet_count = {}
    
    
    for char in string:
    
        if char.isalpha():
            
            if char in alphabet_count:
                alphabet_count[char] += 1
            
            else:
                alphabet_count[char] = 1
    
    for letter, count in alphabet_count.items():
        print(count, letter.upper())


input_string = input("Enter a string: ")
print("Occurrences of each alphabet (case insensitive):")
count_alphabets(input_string)
