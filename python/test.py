#create a class ,matrix producing 2-d (of user defined dimensio ) matrices as its instances. it must have class methods to perform the following operation on a pair of matrices via overloading the suitable operators.  
#a). addition of matrices
#b). subtraction of matrices.
#c). multiplication of matrices.
#d). determination of a matrix(of 2*2 or3*3 matrix only)
#e). transpose of a matrix.
#f). upper triangular matrix of the given matrix
#g). lower triangular matrix of the given matrix.

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0]*cols for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def set_element(self, row, col, value):
        self.data[row][col] = value

    def get_element(self, row, col):
        return self.data[row][col]

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_element(i, j, self.get_element(i, j) + other.get_element(i, j))
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_element(i, j, self.get_element(i, j) - other.get_element(i, j))
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must equal the number of rows in the second matrix for multiplication")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square for determinant calculation")
        if self.rows == 1:
            return self.data[0][0]
        elif self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        else:
            determinant = 0
            for j in range(self.cols):
                determinant += ((-1) ** j) * self.data[0][j] * self.get_minor(0, j).determinant()
            return determinant

    def get_minor(self, row, col):
        minor = Matrix(self.rows - 1, self.cols - 1)
        r = 0
        for i in range(self.rows):
            if i == row:
                continue
            c = 0
            for j in range(self.cols):
                if j == col:
                    continue
                minor.set_element(r, c, self.data[i][j])
                c += 1
            r += 1
        return minor

    def upper_triangle(self):
        upper_triangle_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(i, self.cols):
                upper_triangle_matrix.set_element(i, j, self.data[i][j])
        return upper_triangle_matrix

    def lower_triangle(self):
        lower_triangle_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                if j <= i:
                    lower_triangle_matrix.set_element(i, j, self.data[i][j])
        return lower_triangle_matrix

    def transpose(self):
        transposed_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed_matrix.set_element(j, i, self.data[i][j])
        return transposed_matrix

# Function to create a matrix from user input
def create_matrix_from_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = Matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            value = float(input(f"Enter element at [{i+1}][{j+1}]: "))
            matrix.set_element(i, j, value)
    return matrix

# Function to perform addition operation
def addition(matrix1, matrix2):
    try:
        result = matrix1.add(matrix2)
        print("\nAddition:")
        print(result)
    except ValueError as e:
        print(e)

# Function to perform subtraction operation
def subtraction(matrix1, matrix2):
    try:
        result = matrix1.subtract(matrix2)
        print("\nSubtraction:")
        print(result)
    except ValueError as e:
        print(e)

# Function to perform multiplication operation
def multiplication(matrix1, matrix2):
    try:
        result = matrix1.multiply(matrix2)
        print("\nMultiplication:")
        print(result)
    except ValueError as e:
        print(e)

# Function to calculate determinant
def calculate_determinant(matrix):
    try:
        determinant = matrix.determinant()
        print("\nDeterminant:")
        print(determinant)
    except ValueError as e:
        print(e)

# Function to perform upper triangle operation
def upper_triangle(matrix):
    print("\nUpper Triangle:")
    print(matrix.upper_triangle())

# Function to perform lower triangle operation
def lower_triangle(matrix):
    print("\nLower Triangle:")
    print(matrix.lower_triangle())

# Function to perform transpose operation
def transpose(matrix):
    print("\nTranspose:")
    print(matrix.transpose())

# Main program
def main():
    print("Enter details for the first matrix:")
    matrix1 = create_matrix_from_input()

    print("\nEnter details for the second matrix:")
    matrix2 = create_matrix_from_input()

    # Performing operations
    print("\nMatrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    # Menu for operations
    operations = {
        1: addition,
        2: subtraction,
        3: multiplication,
        4: calculate_determinant,
        5: upper_triangle,
        6: lower_triangle,
        7: transpose
    }

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Determinant")
        print("5. Upper Triangle")
        print("6. Lower Triangle")
        print("7. Transpose")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 8:
            break

        operation = operations.get(choice)
        if operation:
            if choice in [1, 2, 3]:
                operation(matrix1, matrix2)
            else:
                operation(matrix1 if choice != 4 else matrix1)
        else:
            print("Invalid choice. Please choose a valid operation.")
            
            
            
  
            
main()