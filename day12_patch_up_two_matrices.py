cols, rows = input().split()
    
m1 = []
for i in range(int(cols)):
    m1.append(input().split())
        
cols, rows = input().split()
    
m2 = []
for i in range(int(cols)):
    m2.append(input().split())
    
for i, val1 in enumerate(m1):
    for j, val2 in enumerate(val1):
        print(int(val2) + int(m2[i][j]), end=' ')
    print()