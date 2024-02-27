s = "w3resource"
res = {}
for i in range(len(s)):
 if s[i] in res:
  res[s[i]] += 1
 else:
  res[s[i]] = 1

print(res)