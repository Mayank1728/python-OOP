data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

res = set()

for _, nest in enumerate(data):
 for key in nest.keys():
  res.add(nest[key])

print(res)