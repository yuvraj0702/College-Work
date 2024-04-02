def copy_file_with_replacement(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            # Read the contents of the input file
            file_contents = file.read()

            # Replace full stops with commas
            replaced_contents = file_contents.replace('.', ',')

            # Open the output file for writing
            with open(output_file, 'w') as output:
                # Write the replaced contents to the output file
                output.write(replaced_contents)
            
            print("File copied successfully with full stops replaced by commas.")
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


# Usage example
input_file_path = 'input.txt'  # Replace 'input.txt' with your input file path
output_file_path = 'output.txt'  # Replace 'output.txt' with your output file path

copy_file_with_replacement(input_file_path, output_file_path)