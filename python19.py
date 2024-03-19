#write a program that acceses the directory as per the users directive and create a new sub directery in that 
import os

def create_subdirectory():
    # Prompting the user for the directory path
    directory_path = input("Enter the directory path where you want to create a new subdirectory: ")

    # Checking if the directory exists
    if not os.path.exists(directory_path):
        print("Error: Directory does not exist.")
        return

    # Prompting the user for the name of the new subdirectory
    new_subdirectory_name = input("Enter the name of the new subdirectory: ")

    # Constructing the full path of the new subdirectory
    new_subdirectory_path = os.path.join(directory_path, new_subdirectory_name)

    # Checking if the subdirectory already exists
    if os.path.exists(new_subdirectory_path):
        print("Error: Subdirectory already exists.")
        return

    try:
        # Creating the new subdirectory
        os.mkdir(new_subdirectory_path)
        print(f"New subdirectory '{new_subdirectory_name}' created successfully in '{directory_path}'.")
    except OSError as e:
        print(f"Error: {e}")

if _name_ == "_main_":
    create_subdirectory()