def count_unique_words(sentence):
    
    words = sentence.split()

    
    unique_words = set(words)

    
    return len(unique_words)

input_sentence = input("Enter a sentence: ")
unique_word_count = count_unique_words(input_sentence)
print("Number of unique words:", unique_word_count)
