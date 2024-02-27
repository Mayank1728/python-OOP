from copy import deepcopy

# 1. sum all items
ls = [10, 35, 23, 14, -7, 90, -2]
res = 0
for val in ls:
 res += val
print(res)

# 2. multiply
res = 1
for val in ls:
 res = res * val
print(res)


# find min
m = min(ls)


# len is greater than 2 and start and end indexes have same value
data = ["abc", "xyz", "aba", "1221"]
count = 0
for val in data:
 if len(val) >= 2 and val[0] == val[-1]:
  count += 1

print(count)


# sort the set by last ele
data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
data.sort(key = lambda x: x[1])
print(data)

# remove dup from list
data = [1,2,3,4,2,1,1,1,1,3,3,4,4,4,4,7]
s = set()
for val in data:
 if val not in s:
  s.add(val)

print(list(s))

# clone / copy a list
arr = [1,2,2,2,2,22,2,]
a = deepcopy(arr)
arr[0] = 100
print(a) # no changes made here

# list of words longer than n
n = 6
ls = ["Hello", "world", "Demon", "Slayer", "NCAA", "PyThOn", "all_lower_"]
res = []
for val in ls:
 if len(val) >= n:
  res.append(val)
print(res)


# return true if 2 list have 1 comm mem
s = set()
for val in ls:
 s.add(val)

for val in res:
 if val in s:
  print(True)
  break
print(False)


# remove specific index list
res = []
for i,val in enumerate(ls):
 if i == 0 or i == 4 or i == 5:
  pass
 else:
  res.append(val)
print(res)

# print all permutations of list

# difference between the 2 lists


# append list to another list
res = ["holy", "cow", "Howdy", "HO"]
for val in ls:
 res.append(val)
print(res)

# check if 2 lists are circularly identical
ls = [1,3, 4,5, 2]
arr = [4,5,2,1,3]
res = deepcopy(ls)
for val in ls:
 res.append(val)

ls = res
print(ls)
cont = 0
l, r = 0, 0
while(l < len(ls) and r < len(arr)):
 if arr[r] == ls[l]:
  cont += 1
  r += 1
 else:
  cont = 0
  r = 0
 l += 1

if r == len(arr):
 print("Yes its circular")
else: 
 print("Its aint!")


# write a python program to split a list based on first character
 

# 17. remvoe dup from nested list
s = set()
ls = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# because lists and sets are mutable we cannot 
# hash them or add to set
# thats why we convert lists to tuple and 
# sets to frozen set
for val in ls:
 p = tuple(val)
 s.add(p)

res = []
for val in s:
 p = list(val)
 res.append(p)

print(res)



# 

























