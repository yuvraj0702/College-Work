def get_matrix_from_user():
    dimensions = input("Enter the dimensions of the matrix (rows x cols), separated by 'x': ")
    rows, cols = map(int, dimensions.split('x'))
    
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(rows):
        row = tuple(map(int, input(f"Enter elements for row {i+1} (separated by space): ").split()))
        if len(row) != cols:
            print("Invalid number of elements for the row. Please try again.")
            return get_matrix_from_user()
        matrix.append(row)
    return matrix

def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        print("Cannot multiply matrices. Inner dimensions must match.")
        return None
    
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            element = 0
            for k in range(len(matrix_b)):
                element += matrix_a[i][k] * matrix_b[k][j]
            row.append(element)
        result.append(tuple(row))
    return tuple(result)

def main():
    print("Enter the first matrix:")
    matrix_a = get_matrix_from_user()
    print("Enter the second matrix:")
    matrix_b = get_matrix_from_user()

    print("Matrix A:", matrix_a)
    print("Matrix B:", matrix_b)

    product = multiply_matrices(matrix_a, matrix_b)
    if product:
        print("Product of the matrices:", product)

if __name__ == "__main__":
    main()
