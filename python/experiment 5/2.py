def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print("Total number of vowels:", vowel_count)
