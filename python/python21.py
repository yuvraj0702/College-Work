def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print("Content has been successfully written to the file.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to write to file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = "favorite_character.txt"
    content = """My favorite character is Sherlock Holmes. 
    Sherlock Holmes is a fictional detective created by British author Sir Arthur Conan Doyle. 
    He is known for his brilliant deductive reasoning, keen observation, and astute logical reasoning skills."""
    
    write_to_file(file_name, content)


main()