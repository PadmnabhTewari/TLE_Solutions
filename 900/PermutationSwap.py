from math import gcd
for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    b=0
    for j in range(a):
        b=gcd(abs(l[j]-(j+1)),b)
    print(b)
 
