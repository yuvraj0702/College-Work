def first_five_multiples(k):
    multiples = [k * i for i in range(1, 6)]
    return multiples

# Example usage:
k = 3
multiples_list = first_five_multiples(k)
print("First five multiples of", k, ":", multiples_list)
