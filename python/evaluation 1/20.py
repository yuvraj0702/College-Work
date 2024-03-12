def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        return file
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("An error occurred:", str(e))
    return None

def main():
    while True:
        print("\nMenu:")
        print("1. Open file in read mode")
        print("2. Open file in write mode")
        print("3. Open file in append mode")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            file_name = input("Enter file name to open: ")
            file = open_file(file_name, 'r')
            if file:
                print("File opened in read mode.")
                file.close()
        elif choice == '2':
            file_name = input("Enter file name to open: ")
            file = open_file(file_name, 'w')
            if file:
                print("File opened in write mode.")
                file.close()
        elif choice == '3':
            file_name = input("Enter file name to open: ")
            file = open_file(file_name, 'a')
            if file:
                print("File opened in append mode.")
                file.close()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


main()