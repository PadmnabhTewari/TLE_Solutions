import math
for i in range(int(input())):
        n=list(map(int,input().split()))
        arr=list(map(int,input().split()))
        arr.sort()
        r=len(arr)-1
        l=0
        mid=0
        while l <=r:
            e= math.ceil ( (n[0]+1) / 2)
            mid+=arr[r-e +1]
            r-=e
            l+=n[0]-e
        print(mid)
