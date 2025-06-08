from math import *
for _ in range(int(input())):
    n = int(input())
    a = 1
    j = 0
    for i in range(2,int(sqrt(n))+1):
        if (n % i == 0):
            a = n // i
            j = i
            break
    print(a,n-a)
