import bisect
l=[]
for i in range(33):
    l.append(2**i)
for _ in range(int(input())):
    n=int(input())
    a=bisect.bisect_left(l,n)
    b=l[a-1]
    for j in range(b-1,-1,-1):
        print(j,end=" ")
    for j in range(b,n):
        print(j,end=" ")
    print()
