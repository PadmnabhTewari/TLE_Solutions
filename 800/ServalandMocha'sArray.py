from math import gcd
for i1 in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k="NO"
    for i in range(n):
        for j in range(i+1,n):
            if(gcd(a[i],a[j])<=2):
                k="YES"
                
                
    print(k)
