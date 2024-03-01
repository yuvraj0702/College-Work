#using list 
def get_matrix_from_user():
    matrix = []
    print("Enter the elements of the matrix (2x4):")
    for i in range(2):
        row = []
        for j in range(4):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def add_matrices(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] - matrix_b[i][j])
        result.append(row)
    return result

def main():
    print("Using lists:")
    matrix_a = get_matrix_from_user()
    matrix_b = get_matrix_from_user()

    print("Matrix A:", matrix_a)
    print("Matrix B:", matrix_b)

    sum_matrix = add_matrices(matrix_a, matrix_b)
    difference_matrix = subtract_matrices(matrix_a, matrix_b)

    print("Sum of the matrices:", sum_matrix)
    print("Difference of the matrices:", difference_matrix)

if __name__ == "__main__":
    main()
