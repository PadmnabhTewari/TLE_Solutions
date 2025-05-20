for i in range(int(input())):
    a,b,n=map(int,input().split())
    l=list(map(int,input().split()))
    s=b
    for i in range(n):
        s+=min(l[i],a-1)
    print(s)
