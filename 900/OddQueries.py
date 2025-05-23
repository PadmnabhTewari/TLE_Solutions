import itertools 
for i in range(int(input())):
    a,b=map(int, input().split())
    l=list(map(int, input().split()))
    s=sum(l)
    d=[0]
    d1=list(itertools.accumulate(l))
    d=d+d1
    for j in range(b):
        m,n,o=map(int,input().split())
        p=s-(d[n]-d[m-1])+o*(n-m+1)
        if(p%2==0):
            print('NO')
        else:
            print('YES')
