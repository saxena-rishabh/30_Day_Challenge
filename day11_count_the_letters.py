s =input()
u = 0
l = 0
for i in s:
    if i.islower():
        l += 1
    if i.isupper():
        u += 1
print(u)
print(l)