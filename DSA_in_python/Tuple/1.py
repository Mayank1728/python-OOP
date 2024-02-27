# 1. create a tuple
t = (10, -20, 40)

# 2. create a tuple with diff data types
t = ("h", -3.45, 56, 0,True, "Helen", 0)
print(t)

# 3. unpack tuple

# 4. create the colon of a tuple


# 5. find repeated items of a tuple
ls = list(t)
res = []
s = set()
for val in ls:
 if val in s:
  res.append(val)
 else:
  s.add(val)
print(res)

# 6. find and element in tuple
res = "Keller"
for val in t:
 if t == res:
  print("Found")
print("Not found")

# 7. list to tuple
# ls = []
# t = tuple(ls)


# 8. remove item from tuple
l = []
rem = -3.45
for val in t:
 if val != rem:
  l.append(val)
t = tuple(l)
print(t)


# 9. slice a tuple
ls = list(t)
ls = ls[:4]
t = tuple(ls)
print(t)

# 10. reverse a tuple
ls = list(t)
ls.reverse()
t = tuple(ls)
print(t)
