import math

volume_of_cone = lambda r, h: (1/3) * math.pi * r**2 * h

# Example usage:
radius = 3
height = 5
volume = volume_of_cone(radius, height)
print("Volume of cone:", volume)
