from math import pi

def circle_area(r):
    if type(r) not in [float, int]:
        raise TypeError("radius must be int/float")

    if r < 0:
        raise ValueError('radius cannot be negative')

    return pi*(r**2)