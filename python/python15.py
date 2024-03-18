with open("sample_file.txt", "w") as file:
    # Write a few lines to the file
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

# Open file using open() without write mode
with open("sample_file.txt") as file:
    # Read lines from the file
    lines = file.readlines()

# Print the lines read from the file
for line in lines:
    print(line, end='')

# Append more lines to the file without using write()
with open("sample_file.txt", "a") as file:
    file.write("This is line 4\n")
    file.write("This is line 5\n")

# Open the file again to verify the appended lines
with open("sample_file.txt") as file:
    lines = file.readlines()

# Print the updated content of the file
print("\nUpdated content of the file:")
for line in lines:
    print(line, end='')