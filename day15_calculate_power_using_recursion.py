n, p = [int(i) for i in input().split()]
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a,b - 1)
print(power(n,p))