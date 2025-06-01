import math
for i in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    m=0
    for j in range(a):
        s=s+math.ceil(l[j]/b)
        m=m+l[j]
    print(math.ceil(m/b),s)
        
