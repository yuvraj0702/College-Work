# Open the file
with open('in-name.txt', 'r') as file:
    names = file.readlines()

# Count the number of names
num_names = len(names)

# Count the number of names starting with a vowel
num_vowel_starting_names = sum(1 for name in names if name.strip().lower()[0] in 'aeiou')

# Find the longest name
longest_name = max(names, key=lambda x: len(x.strip()))

# Display results
print("a. Count of names:", num_names)
print("b. Count of names starting with a vowel:", num_vowel_starting_names)
print("c. Longest name:", longest_name.strip()) 