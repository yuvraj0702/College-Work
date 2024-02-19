# Define a lambda function to calculate the area of a rectangle
calculate_area = lambda length, breadth: length * breadth

# Example usage:
length = float(input("Enter the length of the plot: "))
breadth = float(input("Enter the breadth of the plot: "))

area = calculate_area(length, breadth)
print("Area of the plot:", area)
