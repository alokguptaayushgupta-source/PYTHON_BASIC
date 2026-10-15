s1 = {23,4,6,9,99,9,44,1}
s2 = {4,6,8,7,34,23,55,65,43}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print({1,4}.issubset(s1))
print({1,4}.issubset(s2))
print(s2.issuperset({65,55,4}))
print(s2.issuperset({63,55,4}))