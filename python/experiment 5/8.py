def main():
    
    S1 = {"Red", "Yellow", "Orange", "Blue"}
    S2 = {"Violet", "Blue", "Purple"}

    
    union_set = S1.union(S2)
    intersection_set = S1.intersection(S2)
    difference_S1_S2 = S1.difference(S2)
    difference_S2_S1 = S2.difference(S1)
    symmetric_difference = S1.symmetric_difference(S2)

    
    print("Set S1:", S1)
    print("Set S2:", S2)
    print("Union of S1 and S2:", union_set)
    print("Intersection of S1 and S2:", intersection_set)
    print("Difference of S1 and S2:", difference_S1_S2)
    print("Difference of S2 and S1:", difference_S2_S1)
    print("Symmetric difference of S1 and S2:", symmetric_difference)

if __name__ == "__main__":
    main()
