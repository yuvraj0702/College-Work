###write the function count vowel (word) which takes the word as the argument and returns the count of vowels in that word  
def count_vowel(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Example usage:
word = "Hello World"
print("Number of vowels in '{}': {}".format(word, count_vowel(word)))  # Output: Number of vowels in 'Hello World': 3
