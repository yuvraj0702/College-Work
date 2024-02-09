def print_words_separate_lines(sentence):
    words = sentence.split()
    for word in words:
        print(word)

input_sentence = input("Enter a sentence: ")
print("Words in separate lines:")
print_words_separate_lines(input_sentence)
