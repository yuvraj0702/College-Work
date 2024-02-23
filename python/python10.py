##write a function count [b(word)] that takes word as the argument and returns the number of b in that word
def count_b(word):
    count = 0
    for char in word:
        if char == 'b' or char == 'B':
            count += 1
    return count

# Example usage:
word = "banana"
print("Number of 'b' in", word, ":", count_b(word))  # Output: 1
