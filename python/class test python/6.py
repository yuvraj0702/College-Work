#write a program that creates tuples with two fields referring to x and y coordinates in a 2-d cartesian space.create four such variables denoting four points in the plane.determine and print the euclidean distances between these points and the lines of equation passing through the pairs of points using a user degined function. the same function must print the angle between the lines too.based on the length of sides computed by this function,you should invoke another function from within the current function that determines whether the quadrilateral formed is a regular one.
def euclidean_distance(point1, point2):
    distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
    return distance

def angle_between_lines(point1, point2, point3, point4):
    slope1 = (point2[1] - point1[1]) / (point2[0] - point1[0])
    slope2 = (point4[1] - point3[1]) / (point4[0] - point3[0])

    angle_radians = abs(slope2 - slope1) / (1 + slope1 * slope2)
    angle_degrees = angle_radians * 180 / 3.14159
    
    return angle_degrees

def is_regular_quadrilateral(distances):
    return all(distance == distances[0] for distance in distances)

if __name__ == "__main__":
    # Define four points
    point1 = (1, 1)
    point2 = (4, 5)
    point3 = (7, 3)
    point4 = (2, 6)

    # Calculate distances between points
    distances = [
        euclidean_distance(point1, point2),
        euclidean_distance(point2, point3),
        euclidean_distance(point3, point4),
        euclidean_distance(point4, point1)
    ]

    # Calculate angles between lines
    angle1 = angle_between_lines(point1, point2, point3, point4)
    angle2 = angle_between_lines(point2, point3, point4, point1)
    angle3 = angle_between_lines(point3, point4, point1, point2)
    angle4 = angle_between_lines(point4, point1, point2, point3)

    # Print distances and angles
    print("Distances between points:", distances)
    print("Angles between lines:", angle1, angle2, angle3, angle4)

    # Check if the quadrilateral is regular
    if is_regular_quadrilateral(distances):
        print("The quadrilateral is regular.")
    else:
        print("The quadrilateral is not regular.")
