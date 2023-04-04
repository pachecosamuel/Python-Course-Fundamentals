def cylinder_area(radius, height):
    def circle_area(radius):
        return pow(radius, 2) * 3.141592;

    return circle_area(radius) * height;

radius = float(input("Type the cylinder's radius: "));
height = float(input("Type the cylinder's height: "));
print(f"The area of the cylinder is: {cylinder_area(radius, height)}");