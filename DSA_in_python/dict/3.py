dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
res = {}

def add_to_res(dict):
 for key in dict.keys():
  if key in res:
   res[key] += dict[key]
  else:
   res[key] = dict[key]

add_to_res(dict1)
add_to_res(dict2)
add_to_res(dict3)
print(res)     