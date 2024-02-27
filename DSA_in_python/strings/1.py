# cal len of str
s = "UCB, UCLA, Umich, UTAustin"
print(len(s))

# count characters
d = {}
s = "google.com"
for val in s:
    if val in d:
        d[val] += 1
    else:
        d[val] = 1
print(d)

# change next occ of all first char
s = "mestmartmmmmt"
change = s[0]
flag = 0
res = []
for i, val in enumerate(s):
    if i != 0 and val == change:
        res.append("$")
    else:
        res.append(val)
res = "".join(res)
print(res)

#
