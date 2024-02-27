from copy import copy, deepcopy

# 1. create a set
s = set()

# 2. iterate over sets
for i in range(20):
 if i < 10:
  s.add(i)
 else:
  s.add(i - 5)
for val in s:
 print(val)


t = deepcopy(s)
# 3. add into set
s.add(17)

# 4. remove from set
s.remove(17)

# 5. remove if present in set
val = 10
if val in s:
 s.remove(val)
print(s)
print(t)

# 6. intersection of set
res = set()
for val in s:
 if val in t:
  res.add(val)

print(res)


# 7. union
union = set()
for val in s: 
 union.add(val)
for val in t:
 union.add(val)
print(union)

# 8. set diff
diff = set() # s - t
s = {1, 2, 3, 4,5}
t = {4,5,6, 7,1}
for val in s:
 if val in t:
  pass
 else:
  diff.add(val)
print(diff)

# 9. what is symmetric diff


# 10. clear a set
diff.clear()

# 11. what are frozenset ?

# 12. find max and min in a set
max_of_s = max(s)
min_of_s = min(s)
m = int("-inf")
for val in s:
 if val > m:
  m = val
print(m)


