def power_set(input_set):
    if len(input_set) == 0:
        return [[]]  # Base case: Power set of an empty set is a set containing an empty set
    else:
        element = input_set.pop()  # Remove one element from the set
        subsets = power_set(input_set)  # Recursively generate power set for the remaining set
        new_subsets = []
        for subset in subsets:
            new_subset = subset.copy()
            new_subset.append(element)  # Include the removed element in each subset
            new_subsets.append(new_subset)
        return subsets + new_subsets

def main():
    user_input = input("Enter the elements of the set separated by spaces: ")
    input_set = set(user_input.split())
    input_set = list(map(int, input_set))  # Convert the input to integers if needed
    input_set.sort()  # Sort the set for consistent output
    result = power_set(input_set)
    print("Power set of", input_set, "is:")
    for subset in result:
        print(subset)

if __name__ == "__main__":
    main()
