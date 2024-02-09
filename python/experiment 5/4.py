def count_substring_occurrences(string, substring):
    count = 0
    sub_len = len(substring)
    for i in range(len(string) - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count


input_string = input("Enter a string: ")
input_substring = input("Enter a substring: ")

occurrences = count_substring_occurrences(input_string, input_substring)
print("Number of times the substring occurs:", occurrences)
