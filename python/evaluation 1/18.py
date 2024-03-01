#accept 2 matix of 2x4 dimension from the user at the runtime 
#a) using as list 
#b) using as tuple
# and perform addition and substraction of the matrixes through different user defined function

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def main():
    # Accept matrices as lists
    print("Enter elements for matrix 1 (2x4) as list:")
    matrix1_list = [[int(input()) for i in range(4)] for i in range(2)]

    print("Enter elements for matrix 2 (2x4) as list:")
    matrix2_list = [[int(input()) for i in range(4)] for i in range(2)]

    # Accept matrices as tuples
    print("Enter elements for matrix 1 (2x4) as tuple:")
    matrix1_tuple = tuple(tuple(int(input()) for i in range(4)) for i in range(2))

    print("Enter elements for matrix 2 (2x4) as tuple:")
    matrix2_tuple = tuple(tuple(int(input()) for i in range(4)) for i in range(2))

    # Perform addition and subtraction
    addition_result_list = add_matrices(matrix1_list, matrix2_list)
    subtraction_result_list = subtract_matrices(matrix1_list, matrix2_list)

    addition_result_tuple = add_matrices(matrix1_tuple, matrix2_tuple)
    subtraction_result_tuple = subtract_matrices(matrix1_tuple, matrix2_tuple)

    # Display results
    print("Addition result (using lists):")
    for row in addition_result_list:
        print(row)

    print("Subtraction result (using lists):")
    for row in subtraction_result_list:
        print(row)

    print("Addition result (using tuples):")
    for row in addition_result_tuple:
        print(row)

    print("Subtraction result (using tuples):")
    for row in subtraction_result_tuple:
        print(row)


main() 