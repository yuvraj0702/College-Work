def main():
    
    n = int(input("Enter the number of fruits: "))

    
    print("Enter fruits for set s1:")
    s1 = set(input("Enter fruit {}:".format(i + 1)) for i in range(n))

    print("Enter fruits for set s2:")
    s2 = set(input("Enter fruit {}:".format(i + 1)) for i in range(n))

    
    common_fruits = s1.intersection(s2)
    print("Fruits which are in both sets s1 and s2:", common_fruits)


    unique_to_s1 = s1.difference(s2)
    print("Fruits only in s1 but not in s2:", unique_to_s1)
    
    total_fruits = len(s1.union(s2))
    print("Count of all fruits from s1 and s2:", total_fruits)

if __name__ == "__main__":
    main()
