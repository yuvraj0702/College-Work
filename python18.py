def count_character(filename, character):
    try:
        with open(filename, "r") as file:
            content = file.read()
            count = content.count(character)
            print(f"The character '{character}' appears {count} times in the file.")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

# Accept filename and character from the user
filename = input("Enter the filename: ")
character = input("Enter the character to count: ")

# Call the function to count the character in the file
count_character(filename, character) 