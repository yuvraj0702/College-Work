def power_set(s):
    """
    Function to compute the power set of a set using recursion.
    """
    if not s:
        return {frozenset()}  # return a set containing an empty set

    element = s.pop()  # remove an element from the set
    subsets = power_set(s)  # compute the power set of the remaining set recursively
    return subsets.union({subset | {element} for subset in subsets})

def input_set():
    """
    Function to take set input from the user.
    """
    elements = input("Enter the elements of the set separated by spaces: ").split()
    return {elem for elem in elements}

def main():
    user_set = input_set()
    user_power_set = power_set(user_set)
    print("Power set of the entered set:")
    for subset in user_power_set:
        print(subset)


main()