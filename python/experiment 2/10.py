
def bitwise_truth_table(operator):
    print(f"Truth Table for {operator.__name__} operator:")
    print(" A | B | Result")
    print("-------------")

    for A in range(2):
        for B in range(2):
            result = operator(A, B)
            print(f" {A} | {B} | {result}")

    print("\n")

bitwise_truth_table(lambda a, b: a & b)  
bitwise_truth_table(lambda a, b: a | b)  
bitwise_truth_table(lambda a, b: a ^ b)  