def process_data(input_string, N):
    processed_string = ''
    capitalize_next = False

    for char in input_string:
        if char == '.':
            capitalize_next = True
        elif char.isdigit():
            processed_string += '[' + char + ']'
            capitalize_next = False
        elif capitalize_next:
            processed_string += char.upper()
            capitalize_next = False
        else:
            processed_string += char

    return processed_string


def write_processed_data(input_string, output_file, N):
    processed_string = process_data(input_string, N)

    try:
        with open(output_file, 'w') as file:
            file.write(processed_string)
        print("Data written to '{}' successfully.".format(output_file))
    except Exception as e:
        print("An error occurred:", str(e))


# Usage example
input_string = "This is a test. 123. This is another test. 456."
output_file_path = 'processed_data.txt'  # Replace 'processed_data.txt' with your output file path
N = 2  # Specify N value

write_processed_data(input_string, output_file_path, N) 