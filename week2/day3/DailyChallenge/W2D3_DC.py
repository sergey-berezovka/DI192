import math

class Circle:
    
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2
        else:
            raise ValueError("You must provide radius or diameter.")
    
    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    def area(self):
        return math.pi * self._radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius:.2f})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius
    
c1 = Circle(radius=3)
c2 = Circle(diameter=8)

print(c1)
print("Area:", c1.area())

c3 = c1 + c2
print("New circle after addition:", c3)

print("c1 > c2:", c1 > c2)
print("c1 == c2:", c1 == c2)

circles = [c1, c2, c3]
circles.sort()

print("Sorted circles:")
for c in circles:
    print(c)