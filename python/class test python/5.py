def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length")

    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result

# Main program
if __name__ == "__main__":
    # Define two vectors
    vector1 = (2, 3, 4, 5, 6)
    vector2 = (1, 2, 1, 2, 1)

    # Calculate dot product using Gauss method
    result_dot_product = dot_product(vector1, vector2)

    # Output the result
    print("Vector 1:", vector1)
    print("Vector 2:", vector2)
    print("Dot product using Gauss method:", result_dot_product)
