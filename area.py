import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def diameter(self):
        return self.radius * 2

    def perimeter(self):
        """Returns the circumference of the circle."""
        return 2 * math.pi * self.radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * self.radius ** 2

my_circle = Circle(radius=7)
print(f"Diameter: {my_circle.diameter()}")
print(f"Perimeter: {my_circle.perimeter():.4f}")
print(f"Area: {my_circle.area():.4f}")