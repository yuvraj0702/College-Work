def dot(one,two):
    dotproduct = 0
    for i in range(len(one)):
        dotproduct += (one[i] * two[i])


    return dotproduct

vector1 = (3,4)
vector2 = (4,3)

print(dot(vector1,vector2))