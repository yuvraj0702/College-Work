##write a function to count letter (word,letter) that takes a word and letter as its arguments and returns the number of occurrence of that letter in that word.
def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

# Example usage:
word = "banana"
letter = "a"
print("Number of '{}' in '{}' : {}".format(letter, word, count_letter(word, letter)))  # Output: Number of 'a' in 'banana' : 3


