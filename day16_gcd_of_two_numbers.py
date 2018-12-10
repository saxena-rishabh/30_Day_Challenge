nos = input()
nos = nos.split(sep=' ')
a = int(nos[0])
b = int(nos[1])
divisor = []
end = min(a, b)
for i in range(1, end+1):
    if a % i == 0 and b % i == 0:
        divisor.append(i)
gcd = max(divisor)
print(gcd)