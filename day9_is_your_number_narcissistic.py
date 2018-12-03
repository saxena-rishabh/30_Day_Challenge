s = input()
a = len(s)
sum = 0
for i in s:
    n = int(i)
    sum += n ** a
if sum == int(s):
    print('True')
else:
    print('False')