##write the function eliminate letter(word,letter) which takes the word and the letter as arguments and remove all occurrences of that letter from the word .the function should also return  the remaining letter in the word 

def eliminate_letter(word, letter):
    remaining_letters = ""
    for char in word:
        if char != letter:
            remaining_letters += char
    return remaining_letters

# Example usage:
word = "banana"
letter = "a"
remaining_word = eliminate_letter(word, letter)
print("Remaining letters in '{}' after eliminating '{}': {}".format(word, letter, remaining_word))  # Output: Remaining letters in 'banana' after eliminating 'a': bnn
