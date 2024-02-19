#write a program that computes the simple interest with a default rate of interest 8.5 percent 
def compute_simple_interest(principal, time, rate=8.5):
    """
    Function to compute simple interest.

    Parameters:
        principal (float): The principal amount.
        time (float): The time period (in years).
        rate (float): The rate of interest (default is 8.5%).

    Returns:
        float: The simple interest.
    """
    interest = (principal * time * rate) / 100
    return interest

# Example usage:
principal_amount = float(input("Enter the principal amount: "))
time_period = float(input("Enter the time period (in years): "))

simple_interest = compute_simple_interest(principal_amount, time_period)
print("Simple Interest:", simple_interest)
