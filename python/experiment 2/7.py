try:
    seconds_input = int(input("Enter the number of seconds: "))
    
    if seconds_input < 0:
        raise ValueError("Please enter a non-negative number of seconds.")
    
    hours = seconds_input // 3600
    minutes = (seconds_input % 3600) // 60
    remaining_seconds = seconds_input % 60

    print(f"{seconds_input} seconds is equal to {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")

except ValueError as e:
    print(f"Error: {e}")
