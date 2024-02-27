L = [32, 34, 100, 2, -9, 45]

print(L[2]) # value at last index 5
print(L[-1]) # value at last index
"""
Everything is object even functions
  ["A" , "BCD" , 14, 8.96, True]
    0      1     2     3     4
    -5     -4    -3    -2    -1
  Alias indexes for the lists
  Lists can store different data types together
  implemented as LinkedList internally
""" 
print(min(L), len(L))
L.append(1000)
L.pop()
print(L.count("The"))



print(L)