from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2
        print(self.p1.x, self.p1.y,
              self.p2.x, self.p2.y)

    def size(self):
        dist = sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)
        self.size = round(dist, 2)
        return self.size

    def __gt__(self, other):
        return self.size() > other.size()

    def __eq__(self, other):
        return self.size() == other.size()

    def __lt__(self, other):
        return self.size() < other.size()


a = Point(5, 10)
b = Point(2, -1)
ab = Line(a, b)
c = Point(5, 10)
d = Point(2, -1)
cd = Line(c, d)
print(ab == cd)
