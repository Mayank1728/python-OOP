from math import sqrt


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def distance(self, other):
        x_diff = (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        return round(sqrt(x_diff + y_diff), 4)


c = Coordinate(3, 4)
zero = Coordinate(0, 0)
print(type(5) == int)
print(c)

# like print u can override these special operators to
# work with +, - , == , <, >, len()
"""
Use assert for type checking
throw error if type is not consistent
__str__ object representation
repr


"""
