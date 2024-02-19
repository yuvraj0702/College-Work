def eval_Quadratic(a, b, c, x):
    return a * x ** 2 + b * x + c


a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))
x = float(input("Enter the value of x: "))

result = eval_Quadratic(a, b, c, x)
print(f"The result of the quadratic equation {a}x^2 + {b}x + {c} for x = {x} is: {result}")