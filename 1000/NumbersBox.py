for _ in range(int(input())):
    a,b=map(int,input().split())
    c=0
    s=0
    mi=10000000000
    for i in range(a):
        l=list(map(int,input().split()))
        for j in l:
            if(j<0):
                c=c+1
            mi = min(mi, abs(j))
            s=s+abs(j)
    if(c%2==1):
        print(s-2*mi)
    else:
        print(s)

 
