from math import pi

def circle_area(radius):
    return pi * radius ** 2

radius = [3.4, 5, 2.4, 11.3, 1.5]

areas = map(circle_area, radius)
optimized_areas = map(lambda r: pi * r ** 2, radius)

print(list(areas))
print(list(optimized_areas))