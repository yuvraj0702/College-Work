import cmath

try:

    a = float(input("Enter the coefficient 'a': "))
    b = float(input("Enter the coefficient 'b': "))
    c = float(input("Enter the coefficient 'c': "))
    

    discriminant = b**2 - 4*a*c
    
    
    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print(f"The roots are real and different: {root1} and {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"The root is real and same: {root}")
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print(f"The roots are complex: {root1} and {root2}")

except ValueError as e:
    print(f"Error: {e}")
