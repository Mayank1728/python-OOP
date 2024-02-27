from math import sqrt

x1, y1 = 3, 4
x2, y2 = 0, -2

# Distance between 2 points
line_1 = round(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 4)
print("Length of first line is: ", line_1)

p1, q1 = 9, 0
p2, q2 = 7, 3

line_2 = round(sqrt((p1 - p2) ** 2 + (q1 - q2) ** 2), 4)
print("Length of second line is: ", line_2)

print("Are the 2 lines equal? ", line_1 == line_2)
