def dot_product(vector1, vector2):
    if len(vector1) != 5 or len(vector2) != 5:
        raise ValueError("Vectors must be of length 5")
    
    result = 0
    for i in range(5):
        result += vector1[i] * vector2[i]
    
    return result

# Main program
if __name__ == "__main__":
    # Define two vectors
    vector1 = (1, 2, 3, 4, 5)
    vector2 = (6, 7, 8, 9, 10)

    # Calculate dot product
    result_dot_product = dot_product(vector1, vector2)

    # Output the result
    print("Vector 1:", vector1)
    print("Vector 2:", vector2)
    print("Dot product:", result_dot_product)
