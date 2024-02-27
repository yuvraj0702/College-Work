#def add_complex(complex1, complex2):
    real_part = complex1[0] + complex2[0]
    imag_part = complex1[1] + complex2[1]
    return (real_part, imag_part)

def subtract_complex(complex1, complex2):
    real_part = complex1[0] - complex2[0]
    imag_part = complex1[1] - complex2[1]
    return (real_part, imag_part)

def multiply_complex(complex1, complex2):
    real_part = complex1[0] * complex2[0] - complex1[1] * complex2[1]
    imag_part = complex1[0] * complex2[1] + complex1[1] * complex2[0]
    return (real_part, imag_part)

def divide_complex(complex1, complex2):
    denominator = complex2[0] ** 2 + complex2[1] ** 2
    real_part = (complex1[0] * complex2[0] + complex1[1] * complex2[1]) / denominator
    imag_part = (complex1[1] * complex2[0] - complex1[0] * complex2[1]) / denominator
    return (real_part, imag_part)

def main():
    complex1 = tuple(float(x) for x in input("Enter complex1 (comma-separated values): ").split(','))
    complex2 = tuple(float(x) for x in input("Enter complex2 (comma-separated values): ").split(','))

    result_addition = add_complex(complex1, complex2)
    print("Addition:", result_addition)

    result_subtraction = subtract_complex(complex1, complex2)
    print("Subtraction:", result_subtraction)

    result_multiplication = multiply_complex(complex1, complex2)
    print("Multiplication:", result_multiplication)

    result_division = divide_complex(complex1, complex2)
    print("Division:", result_division)


main()