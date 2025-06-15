import math

for _ in range(int(input())):
    x, y, k =map(int, input().split())
    need=k*y+k
    a=(need-1)//(x-1)
    if((need-1)%(x-1)):
        a=a+1
    a=a+k
    print(a)
 
