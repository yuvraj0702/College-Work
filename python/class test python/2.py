def repeat_word(word):
    repeated_word = word * len(word)
    return repeated_word

# Test the function
input_word = input("Enter a word: ")
repeated_word = repeat_word(input_word)
print("Repeated word based on the number of letters:", repeated_word)
