def copy_first_10_bytes(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, "rb") as input_f:
            # Read the first 10 bytes
            data = input_f.read(10)
            # Open the output file in write mode
            with open(output_file, "wb") as output_f:
                # Write the read data into the output file
                output_f.write(data)
        print("First 10 bytes copied successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

# File paths
input_file = "sample.txt"
output_file = "output.txt"

# Call the function to copy first 10 bytes
copy_first_10_bytes(input_file, output_file)