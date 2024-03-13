def multiply_vectors(vector1, vector2):
    result = []
    for i in range(5):
        result.append(vector1[i] * vector2[i])
    return result


vector1 = []
vector2 = []

print("Enter elements for vector 1:")
for i in range(5):
    element = float(input(f"Enter element {i + 1}: "))
    vector1.append(element)

print("\nEnter elements for vector 2:")
for i in range(5):
    element = float(input(f"Enter element {i + 1}: "))
    vector2.append(element)

result = multiply_vectors(vector1, vector2)
if result:
    print("\nThe result of multiplying the vectors element-wise is:", result)