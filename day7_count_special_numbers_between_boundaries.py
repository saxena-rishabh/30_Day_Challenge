lower = int(input())
upper = int(input())
l = []
for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           l.append(num)
print(len(l))