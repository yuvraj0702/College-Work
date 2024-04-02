def exchange_file_contents(file1, file2):
    try:
        # Open file 1 for reading its contents
        with open(file1, 'r') as f1:
            file1_contents = f1.read()

        # Open file 2 for reading its contents
        with open(file2, 'r') as f2:
            file2_contents = f2.read()

        # Write file 1 contents to file 2
        with open(file2, 'w') as f2:
            f2.write(file1_contents)

        # Write file 2 contents to file 1
        with open(file1, 'w') as f1:
            f1.write(file2_contents)

        print("Contents of {} and {} exchanged successfully.".format(file1, file2))

    except FileNotFoundError:
        print("One or both files not found.")
    except Exception as e:
        print("An error occurred:", str(e))


# Usage example
file1_path = 'file1.txt'  # Replace 'file1.txt' with your first file path
file2_path = 'file2.txt'  # Replace 'file2.txt' with your second file path

exchange_file_contents(file1_path, file2_path)