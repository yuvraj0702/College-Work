def copy_script_without_comments(source_file, destination_file):
    try:
        with open(source_file, "r") as src:
            with open(destination_file, "w") as dest:
                for line in src:
                    if not line.strip().startswith("#"):  # Skip comment lines
                        dest.write(line)
        print("Script copied without comments successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

# File paths
source_file = "source_script.py"
destination_file = "destination_script.py"

# Call the function to copy script without comments
copy_script_without_comments(source_file, destination_file)