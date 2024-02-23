###write a function mirror text(word1,word2) which take 2 word as the arguments and returns a new word like word 1,word1,word2,word2.


def mirror_text(word1, word2):
    return word1 + ',' + word1 + ',' + word2 + ',' + word2

# Example usage:
word1 = "hello"
word2 = "world"
result = mirror_text(word1, word2)
print("Mirror text:", result)  # Output: Mirror text: hello,hello,world,world
